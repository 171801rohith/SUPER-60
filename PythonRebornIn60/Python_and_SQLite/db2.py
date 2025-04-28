from sqlmodel import create_engine, Session, select
from models2 import Hero

engine = create_engine("sqlite:///HeroData2.db", echo=True)


def create_heros():
    h1 = Hero(name="Shetty", secret_name="Kritharth B Shetty", age=19)
    h2 = Hero(name="Krrish", secret_name="Krrish Raj Kushagrey", age=19)
    h3 = Hero(name="Sheik", secret_name="Abhishek H", age=20)

    with Session(engine) as session:
        session.add(h1)
        session.add(h2)
        session.add(h3)
        session.commit()


def select_all_hero():
    with Session(engine) as session:
        query = select(Hero).where(Hero.name == "Krrish")
        response = session.exec(query)
        # print("HERO: ", response.first())
        for hero in response:
            print("HERO: ", hero)

def update_one():
    with Session(engine) as session:
        query = select(Hero).where(Hero.name == "Krrish")
        respone = session.exec(query).first()
        print("Hero age (Before): ", respone.age)
        respone.age = 90
        session.add(respone)
        session.commit()
        session.refresh(respone)
        print("Hero age (After): ", respone.age)

def delete_one():
    with Session(engine) as session:
        query = select(Hero).where(Hero.name == "Krrish")
        respone = session.exec(query).first()
        session.delete(respone)
        session.commit()

def addDataWithParams(name:str,age:int|None,secret:str):
    hero_temp=Hero(name=name,secret_name=secret,age=age)

    with Session(engine) as session:
        session.add(hero_temp)
        session.commit()
        session.refresh(hero_temp)
        print("New item added:",hero_temp)

