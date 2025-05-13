from fastapi import FastAPI, Query
from pydantic import BaseModel
from routes import router
from book import router

app = FastAPI()


# @app.get("/")
# def root():
#     return {"GOOD": "NIGHT"}


# # Query Parameter
# @app.get("/greet")
# def root(name: str = Query(description="Nothing")):
#     # def root(name: str):
#     return {"message": f"Good Evening {name}"}


# @app.get("/calculator")
# def calculator(a: int, b: int):
#     try:
#         div = a / b
#     except Exception as e:
#         div = "Can't Divide by zero"

#     return {
#         "a + b": a + b,
#         "a - b": a - b,
#         "a * b": a * b,
#         "a / b": f"{div}",
#     }


# # Path Parameters
# @app.get("/nothing/{model}")
# def nothing(model: str):
#     return {"NOTHING": f"{model}"}

# class User(BaseModel):
#     username: str
#     email: str

# @app.post("/user")
# def user(user: User):
#     return {"id": 1} + user


app.include_router(router)