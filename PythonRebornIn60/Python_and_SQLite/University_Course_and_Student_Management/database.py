from sqlmodel import SQLModel, create_engine, select
from models import (
    Student,
    StudentCourseLink,
    Department,
    Course,
)

sqlite_url = "sqlite:///universityDB.db"
engine = create_engine(sqlite_url, echo=True)
