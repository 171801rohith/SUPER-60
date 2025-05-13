from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None)


sql_url = "sqlite:///Hero.db"

engine = create_engine(sql_url, echo=True)


def create_db():
    SQLModel.metadata.create_all(engine)


app = FastAPI()

app.on_event("startup")


def on_startup():
    create_db()


@app.post("/heroes/")
def create_hero(hero: Hero):
    with Session(engine) as session:
        session.add(hero)
        session.commit()
        session.refresh(hero)
        return hero


@app.get("/all_heros")
def get_all_heroes():
    with Session(engine) as session:
        heroes = session.exec(select(Hero)).all()
        return heroes
