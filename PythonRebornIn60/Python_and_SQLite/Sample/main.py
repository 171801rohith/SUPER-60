from sqlmodel import SQLModel
from Samole.db2 import *


def create_db():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db()
    # create_heros()
    # select_all_hero()
    update_one()
    addDataWithParams("Nan",-12,"none")
