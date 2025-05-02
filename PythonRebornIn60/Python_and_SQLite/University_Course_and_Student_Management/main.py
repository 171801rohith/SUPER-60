from sqlmodel import SQLModel
from databaseUni import engine, create_course, create_department


def create_db():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    # create_db()

    # create_course("Python", "PY01")
    # create_course("JavaScript", "JS01")

    create_department("CSE")
    create_department("AIML")
