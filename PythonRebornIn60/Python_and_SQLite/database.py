from sqlmodel import create_engine, Session, or_, select
from models import Hero, Team

sqlite_url = "sqlite:///HeroTeamData.db"
engine = create_engine(sqlite_url, echo=True)


def create_heros():
    with Session(engine) as session:
        avengers = Team(team_name="Avengers", head_quarters="Stark Tower")
        xmen = Team(team_name="X-men", head_quarters="X-Mansion")

        # session.add(avengers)
        # session.add(xmen)
        # session.commit()

        deadpool = Hero(
            name="Deadpool",
            secret_name="Wade Wilson",
            age=45,
            # team_id=xmen.id,
            teams=[xmen, avengers],
        )
        iron_man = Hero(
            name="Iron Man",
            secret_name="Tony Stark",
            age=40,
            # team_id=avengers.id,
            teams=[avengers],
        )
        spider_man = Hero(name="Spider Man", secret_name="Peter Parker", age=17)

        session.add_all([deadpool, iron_man, spider_man])
        session.commit()

        red_guardian = Hero(name="Red Guardian", secret_name="Aadithya", age=170)
        winter_soldier = Hero(name="Winter Soldier", secret_name="Bucky Burns", age=185)
        # thunderbolts = Team(
        #     team_name="ThunderBolts*",
        #     head_quarters="Val Tower",
        #     heroes=[red_guardian, winter_soldier],
        # )
        # OR
        thunderbolts = Team(
            team_name="ThunderBolts*",
            head_quarters="Val Tower",
        )
        thunderbolts.heroes.append(red_guardian)
        thunderbolts.heroes.append(winter_soldier)

        session.add(thunderbolts)
        session.commit()


def select_heros():
    with Session(engine) as session:
        # query = select(Hero, Team).where(Hero.team_id == Team.id)
        query = (
            select(Hero, Team).join(Team, isouter=True).where(Hero.team_id == Team.id)
        )
        results = session.exec(query)
        for hero, team in results:
            # for hero in results:
            print("Hero:", hero)
            print("Team:", team)


def delete_heros():
    with Session(engine) as session:
        heros = session.exec(select(Hero)).all()
        teams = session.exec(select(Team)).all()
        for hero in heros:
            session.delete(hero)
            session.commit()
        for team in teams:
            session.delete(team)
            session.commit()


def update_hero():
    with Session(engine) as session:
        query1 = select(Hero).where(Hero.name == "Spider Man")
        query2 = select(Team).where(Team.team_name == "Avengers")
        hero = session.exec(query1).first()
        team = session.exec(query2).first()

        hero.team_id = team.id
        session.add(hero)
        session.commit()
        session.refresh(hero)


def select_():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Winter Soldier")
        result = session.exec(statement)
        spider_man = result.one()

        print(spider_man.team)
