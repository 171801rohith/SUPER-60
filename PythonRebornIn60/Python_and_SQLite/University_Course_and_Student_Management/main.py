from sqlmodel import SQLModel
from database import engine


def create_db():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db()
