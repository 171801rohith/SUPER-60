from sqlmodel import SQLModel, Field, Session, create_engine
from fastapi import FastAPI, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from jwt.exceptions import InvalidTokenError
from typing import Annotated
from passlib.context import CryptContext


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = Field(default=None)


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

app.on_event("startup")


def on_startup():
    create_db_table()


oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")
db_dependency = Annotated[Session, Depends(get_db_connection)]

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
