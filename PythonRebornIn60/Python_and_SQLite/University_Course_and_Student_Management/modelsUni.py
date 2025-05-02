from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional


class StudentCourseLink(SQLModel, table=True):
    student_id: int | None = Field(foreign_key="student.id", primary_key=True)
    course_id: int | None = Field(foreign_key="course.id", primary_key=True)

    enrollment_date: Optional[datetime] = Field(default_factory=datetime.now)
    grade: Optional[str]


class Department(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    name: str = Field(unique=True, index=True)
    building: Optional[str]

    courses: list["Course"] = Relationship(back_populates="department")


class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    first_name: str
    last_name: str
    email: str = Field(unique=True, index=True)

    courses: list["Course"] = Relationship(
        back_populates="students",
        link_model=StudentCourseLink,
    )


class Course(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    title: str = Field(index=True)
    code: str = Field(unique=True, index=True)
    department_id: int | None = Field(foreign_key="department.id", ondelete="CASCADE")

    department: Optional["Department"] = Relationship(back_populates="courses")
    students: list["Student"] = Relationship(
        back_populates="courses",
        link_model=StudentCourseLink,
    )
