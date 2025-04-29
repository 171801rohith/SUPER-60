# Exercise 1: Add Another Model
# Objective: Understand how to define multiple models.
# Task:
# Define this Team model.
# Modify create_db_and_tables() to include this.
# Run the script and verify tables in DB Browser for SQLite

from sqlmodel import Field, SQLModel, Relationship


class HeroTeamLink(SQLModel, table=True):
    # Both act as a composite key
    team_id: int | None = Field(default=None, foreign_key="team.id", primary_key=True)
    hero_id: int | None = Field(default=None, foreign_key="hero.id", primary_key=True)


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    team_name: str = Field(index=True)
    head_quarters: str

    # heroes: list["Hero"] = Relationship(back_populates="team")  # O to M
    heroes: list["Hero"] = Relationship(back_populates="teams", link_model=HeroTeamLink)


# heroes <---> team - many to one and vice versa


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)  # nullable Column
    # team_id: int | None = Field(default=None, foreign_key="team.id", ondelete="CASCADE") # not required since hero can be a part of many teams

    # team: Team | None = Relationship(back_populates="heroes")  # M to O
    teams: list[Team] = Relationship(back_populates="heroes", link_model=HeroTeamLink)
