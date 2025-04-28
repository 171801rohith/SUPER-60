# Exercise 1: Add Another Model 
# Objective: Understand how to define multiple models.
# Task:
# Define this Team model.
# Modify create_db_and_tables() to include this.
# Run the script and verify tables in DB Browser for SQLite

from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)  # nullable Column
    team_id: int | None = Field(default=None, foreign_key="team.id")


class Team(SQLModel, table=True):
    id: int |  None = Field(default=None, primary_key=True)
    team_name: str = Field(index=True)
    head_quarters: str