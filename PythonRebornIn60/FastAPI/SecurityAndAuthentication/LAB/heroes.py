from datetime import datetime, timedelta, timezone
from sqlmodel import SQLModel, Field, Session, create_engine, select
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import jwt
from jwt.exceptions import InvalidTokenError
from typing import Annotated
from passlib.context import CryptContext


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = Field(default=None)


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    hashed_password: str
    disabled: bool = Field(default=False)


class UserIn(BaseModel):
    username: str
    password: str
    disabled: bool = False


class Token(BaseModel):
    access_token: str
    token_type: str


sql_url = "sqlite:///HEROES_DB.db"
engine = create_engine(sql_url, echo=True)

SECRET_KEY = "2ea2b7ae9e7855b316ab22ce4bb6a2ea2a3d5329a3d78fd32a54b8a865f29259"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20


def get_db_connection():
    db = Session(engine)
    try:
        yield db
    except Exception as e:
        print("Error:", e)
        raise e
    finally:
        db.close()


def create_db_table():
    SQLModel.metadata.create_all(engine)


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_table()


oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")
db_dependency = Annotated[Session, Depends(get_db_connection)]

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(hashed_password, password):
    return pwd_context.verify(password, hashed_password)


def hash_password(password):
    return pwd_context.hash(password)


def authenticate_user(username: str, password: str, db: db_dependency):
    user = db.exec(select(User).where(User.username == username)).first()
    if not user:
        return False
    if not verify_password(user.hashed_password, password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    jwt_encoded = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return jwt_encoded


async def get_current_user(
    token: Annotated[str, Depends(oauth2_schema)], db: db_dependency
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except:
        raise credentials_exception
    user = db.exec(select(User).where(User.username == username)).first()
    if not user:
        raise credentials_exception
    return user


def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive User"
        )
    return current_user


@app.post("/token")
async def login_user(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
) -> Token:
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        {"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="Bearer")


@app.post("/create-user")
async def create_user(user_in: UserIn, db: db_dependency):
    try:
        user = User(
            username=user_in.username,
            hashed_password=hash_password(user_in.password),
            disabled=user_in.disabled,
        )
        db.add(user)
        db.commit()
        return {"detail": "User created"}
    except Exception as e:
        return {"detail": f"Error: {e}"}


@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user


@app.post("/create-hero")
async def create_hero(
    name: str,
    secret_name: str,
    age: int,
    db: db_dependency,
    user: Annotated[User, Depends(get_current_active_user)],
):
    try:
        hero = Hero(name=name, secret_name=secret_name, age=age)
        db.add(hero)
        db.commit()
        return {"detail": "Hero created"}
    except Exception as e:
        return {"detail": f"Error: {e}"}


@app.get("/heroes", response_model=list[Hero])
async def get_heroes(
    db: db_dependency,
    user: Annotated[User, Depends(get_current_active_user)],
):
    return db.exec(select(Hero)).all()
