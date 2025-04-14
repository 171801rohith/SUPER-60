from sqlmodel import create_engine

sqlite_url = "sqlite:///HeroData.db"
engine = create_engine(sqlite_url, echo=True)

