from sqlmodel import SQLModel
from databaseUni import (
    engine,
    create_course,
    create_department,
    create_student,
    add_course_to_department,
    add_course_to_students,
    get_department_by_name,
    get_student_by_email,
    get_course_by_code,
    all_courses,
    all_departments,
    all_students,
    update_student_email,
    delete_course_by_code
)


def create_db():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    # create_db()

    # create_course("Python", "PY01")
    # create_course("JavaScript", "JS01")
    # create_course("Java", "J01")
    # create_course("Easy AIML", "AI01")
    # create_course("Data Analytics", "DA01")
    # create_course("Graph Theory", "GT01", department_id=1)

    # create_department("CSE")
    # create_department("AIML")

    # create_student("Aadithya", "Nayak", "aadithya@gmail.com")
    # create_student("Abhishek", "H", "abhishek@gmail.com")

    # add_course_to_department(["PY01", "J01"], "CSE")
    # add_course_to_department(["AI01", "JS01", "DA01"], "AIML")

    # add_course_to_students(["AI01", "JS01", "DA01"], "aadithya@gmail.com")
    # add_course_to_students([ "J01", "AI01"], "abhishek@gmail.com")

    # get_department_by_name("cse")
    # get_student_by_email("aadithya@gmail.com")
    # get_course_by_code("j01")

    # all_students()
    # all_courses()
    # all_departments()

    # update_student_email("aadithya@gmail.com", "aadithya1234@gmail.com")

    delete_course_by_code("GT01")
