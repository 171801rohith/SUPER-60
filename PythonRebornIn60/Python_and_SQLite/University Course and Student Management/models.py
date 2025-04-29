from sqlmodel import SQLModel, Field, Relationship


class Department(SQLModel, table=True):
    id: 


class Student(SQLModel, table=True):
    pass


class Course(SQLModel, table=True):
    pass


class StudentCourseLink(SQLModel, table=True):
    pass
