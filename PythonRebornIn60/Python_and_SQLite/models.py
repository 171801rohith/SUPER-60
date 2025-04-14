# Exercise 1: Add Another Model 
# Objective: Understand how to define multiple models.
# Task:
# Define this Team model.
# Modify create_db_and_tables() to include this.
# Run the script and verify tables in DB Browser for SQLite

from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None  # nullable Column


class Team(SQLModel, table=True):
    id: int |  None = Field(default=None, primary_key=True)
    team_name: str
    team_strength: int