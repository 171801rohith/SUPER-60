from sqlmodel import SQLModel, create_engine, select, Session
from modelsUni import (
    Student,
    Department,
    Course,
)

sqlite_url = "sqlite:///universityDB.db"
engine = create_engine(sqlite_url, echo=True)


def create_course(title, code):
    with Session(engine) as session:
        course = Course(title=title, code=code)
        session.add(course)
        session.commit()

        print("=" * 80)
        print("Commit Successfull.")
        print("=" * 80)


def create_department(name):
    with Session(engine) as session:
        dept = Department(name=name)
        session.add(dept)
        session.commit()

        print("=" * 80)
        print("Commit Successfull.")
        print("=" * 80)


def create_student(fname, lname, email):
    with Session(engine) as session:
        stud = Student(first_name=fname, last_name=lname, email=email)
        session.add(stud)
        session.commit()

        print("=" * 80)
        print("Commit Successfull.")
        print("=" * 80)


def add_course_to_department(codes, dept_name):
    with Session(engine) as session:
        query = select(Department).where(Department.name == dept_name.upper())
        dept = session.exec(query).one()
        courses = []
        for code in codes:
            query = select(Course).where(Course.code == code.upper())
            course = session.exec(query).one()
            courses.append(course)
        dept.courses = courses
        session.add(dept)
        session.commit()

        print("=" * 80)
        print("Commit Successfull.")
        print("=" * 80)
