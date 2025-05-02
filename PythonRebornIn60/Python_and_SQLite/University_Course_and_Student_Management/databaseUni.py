from sqlmodel import SQLModel, create_engine, select, Session
from modelsUni import Student, Department, Course, StudentCourseLink

sqlite_url = "sqlite:///universityDB.db"
engine = create_engine(sqlite_url, echo=True)


def create_course(title, code, **kwargs):
    with Session(engine) as session:
        course = Course(title=title, code=code, **kwargs)
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
        dept = session.exec(query).first()
        courses = []
        for code in codes:
            query = select(Course).where(Course.code == code.upper())
            course = session.exec(query).first()
            courses.append(course)
        dept.courses = courses
        session.add(dept)
        session.commit()

        print("=" * 80)
        print("Commit Successfull.")
        print("=" * 80)


def enroll_student(student_id, course_id):
    with Session(engine) as session:
        query = select(StudentCourseLink).where(
            StudentCourseLink.student_id == student_id,
            StudentCourseLink.course_id == course_id,
        )
        sc = session.exec(query).first()
        if sc:
            print("=" * 80)
            print("Already Enrolled.")
            print("=" * 80)
        else:
            query = select(Student).where(Student.id == student_id)
            stud = session.exec(query).first()
            if stud:
                query = select(Course).where(Course.id == course_id)
                course = session.exec(query).first()
                if course:
                    stud.courses.append(course)
                    session.add(stud)
                    session.commit()
                    print("=" * 80)
                    print("Commit Successfull.")
                    print("=" * 80)
                else:
                    print("=" * 80)
                    print("Course not in Database.")
                    print("=" * 80)
            else:
                print("=" * 80)
                print("Student not in Database.")
                print("=" * 80)


def get_department_by_name(dept_name):
    with Session(engine) as session:
        query = select(Department).where(Department.name == dept_name.upper())
        dept = session.exec(query).first()
        print("=" * 80)
        if not dept:
            print("Not Found In DataBase.")
        else:
            print(dept)
        print("=" * 80)


def get_student_by_email(email):
    with Session(engine) as session:
        query = select(Student).where(Student.email == email.lower())
        stud = session.exec(query).first()
        print("=" * 80)
        if not stud:
            print("Not Found In DataBase.")
        else:
            print(stud)
        print("=" * 80)


def get_course_by_code(code):
    with Session(engine) as session:
        query = select(Course).where(Course.code == code.upper())
        course = session.exec(query).first()
        print("=" * 80)
        if not course:
            print("Not Found In DataBase.")
        else:
            print(course)
        print("=" * 80)


def all_courses():
    with Session(engine) as session:
        query = select(Course)
        courses = session.exec(query).all()
        print("=" * 80)
        if not courses:
            print("Not Found In DataBase.")
        else:
            for course in courses:
                print(course)
        print("=" * 80)


def all_departments():
    with Session(engine) as session:
        query = select(Department)
        depts = session.exec(query).all()
        print("=" * 80)
        if not depts:
            print("Not Found In DataBase.")
        else:
            for dept in depts:
                print(dept)
        print("=" * 80)


def all_students():
    with Session(engine) as session:
        query = select(Student)
        studs = session.exec(query).all()
        print("=" * 80)
        if not studs:
            print("Not Found In DataBase.")
        else:
            for stud in studs:
                print(stud)
        print("=" * 80)


def update_student_email(oldemail, newemail):
    with Session(engine) as session:
        query = select(Student).where(Student.email == oldemail.lower())
        stud = session.exec(query).first()
        print("=" * 80)
        if not stud:
            print("Not Found In DataBase.")
        else:
            stud.email = newemail
            session.add(stud)
            session.commit()
            print("Update Successfull.")
        print("=" * 80)


def delete_course_by_code(code):
    with Session(engine) as session:
        query = select(Course).where(Course.code == code.upper())
        course = session.exec(query).first()
        print("=" * 80)
        if not course:
            print("Not Found In DataBase.")
        else:
            session.delete(course)
            session.commit()
            print("Deletion Successfull.")
        print("=" * 80)


def get_courses_for_student(student_id):
    with Session(engine) as session:
        query = select(Student).where(Student.id == student_id)
        stud = session.exec(query).first()
        print("=" * 80)
        if not stud:
            print("Not Found In DataBase.")
        else:
            print(stud.courses)
        print("=" * 80)


def get_students_in_courses(course_id):
    with Session(engine) as session:
        query = select(Course).where(Course.id == course_id)
        course = session.exec(query).first()
        print("=" * 80)
        if not course:
            print("Not Found In DataBase.")
        else:
            print(course.students)
        print("=" * 80)


def set_enrollment_grade(student_id, course_id, grade):
    with Session(engine) as session:
        query = select(StudentCourseLink).where(
            StudentCourseLink.student_id == student_id,
            StudentCourseLink.course_id == course_id,
        )
        sc = session.exec(query).first()
        print("=" * 80)
        if not sc:
            print("Not Found In DataBase.")
        else:
            sc.grade = grade
            session.add(sc)
            session.commit()
            print("Grade updated.")
        print("=" * 80)
