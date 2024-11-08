from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    with Session(engine) as session:
        yield session
