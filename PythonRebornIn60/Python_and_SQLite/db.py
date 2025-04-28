from sqlmodel import create_engine, Session, or_, select
from models import Hero

sqlite_url = "sqlite:///HeroData.db"
engine = create_engine(sqlite_url, echo=True)


def create_heros():
    h1 = Hero(name="Deadpool", secret_name="Wade Wilson", age=55)
    h2 = Hero(name="Wolverine", secret_name="Logan", age=235)
    h3 = Hero(name="Iron Man", secret_name="Tony Stark", age=45)
    h4 = Hero(name="Black Panther", secret_name="T'Challa", age=35)
    h5 = Hero(name="Dr. Strange", secret_name="Stephen Strange", age=40)
    h6 = Hero(name="Spider Man", secret_name="Peter Parker", age=25)

    # print("Before interacting with db")
    # print("Hero 1: ", h1)
    # print("Hero 2: ", h2)
    # print("Hero 3: ", h3)

    with Session(engine) as session:
        session.add(h1)
        session.add(h2)
        session.add(h3)
        session.add(h4)
        session.add(h5)
        session.add(h6)

        # session.add_all([h1, h2, h3, h4])

        # print("After interacting with db")
        # print("Hero 1: ", h1)
        # print("Hero 2: ", h2)
        # print("Hero 3: ", h3)

        session.commit()

        # Now these objects will be marked as expired
        # print("After committing with db")
        # print("Hero 1: ", h1)
        # print("Hero 2: ", h2)
        # print("Hero 3: ", h3)

        session.refresh(h1)
        session.refresh(h2)
        session.refresh(h3)

        # print("After refreshing with db")
        # print("Hero 1: ", h1)
        # print("Hero 2: ", h2)
        # print("Hero 3: ", h3)


def select_heros():
    with Session(engine) as session:
        # statement = select(Hero)
        # statement = select(Hero).limit(3)
        statement = select(Hero).offset(4).limit(3)
        results = session.exec(statement).all()

        print("-" * 30)
        for result in results:
            print(result)


def select_heros_where():
    with Session(engine) as session:
        # statement = select(Hero).where(Hero.name == "Iron Man", Hero.age <= 45)
        statement = select(Hero).where(or_(Hero.name == "Iron Man", Hero.age <= 45))
        results = session.exec(statement).all()

        print("-" * 30)
        for result in results:
            print(result)


def one_data():
    with Session(engine) as session:
        # statement = select(Hero)
        # results = session.exec(statement).all()
        # hero = results.one()
        hero = session.get(Hero, 1)
        print("Hero: ", hero)


def delete_heros():
    with Session(engine) as session:
        heros = session.exec(select(Hero)).all()
        for hero in heros:
            session.delete(hero)
            session.commit()


def delete_heros_where():
    with Session(engine) as session:
        results = session.exec(select(Hero).where(Hero.name == "Spider Man"))
        hero = results.one()
        session.delete(hero)
        session.commit()


def update_hero():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider Man")
        results = session.exec(statement)
        hero = results.one()
        print("-" * 45)
        print("Hero: ", hero)
        hero.age = 18
        session.add(hero)
        session.commit()
        session.refresh(hero)
        print("-" * 45)
        print("Updated: ", hero)
