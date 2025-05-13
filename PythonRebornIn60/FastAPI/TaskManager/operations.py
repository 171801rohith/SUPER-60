import csv
from models import Task, TaskWithID

DATABASE_FILE = "tasks.csv"

column_fields = ["id", "title", "description", "status"]


def read_all_task() -> list[TaskWithID]:
    with open(DATABASE_FILE) as csvF:
        reader = csv.DictReader(csvF)
        return [TaskWithID(**row) for row in reader]


def read_task(task_id) -> TaskWithID | None:
    with open(DATABASE_FILE) as csvF:
        reader = csv.DictReader(csvF)
    for row in reader:
        if int(row["id"]) == task_id:
            return TaskWithID(**row)


def get_next_id():
    try:
        with open(DATABASE_FILE, "r") as csvF:
            reader = csv.DictReader(csvF)
            max_id = max(int(row["id"] for row in reader))
            return max_id + 1
    except (FileNotFoundError, ValueError):
        return 1


def write_task_into_csv(task: TaskWithID):
    with open(DATABASE_FILE, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=column_fields)
        writer.writerow(task.model_dump())


def create_tasak(task: Task) -> TaskWithID:
    id = get_next_id()
    task_with_id = TaskWithID(id=id, **task.model_dump())
