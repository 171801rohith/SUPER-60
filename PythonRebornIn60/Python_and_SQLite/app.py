from sqlmodel import SQLModel
import models
# from db import engine, create_heros, select_heros, select_heros_where, delete_heros_where, one_data, update_hero, delete_heros
from database import engine, create_heros, select_heros, delete_heros, update_hero


def create_db_and_table():
    SQLModel.metadata.create_all(engine)


def main():
    create_db_and_table()
    # create_heros()
    # delete_heros()
    # delete_heros_where()
    # select_heros()
    # select_heros_where()
    # one_data()
    update_hero()


if __name__ == "__main__":
    main()