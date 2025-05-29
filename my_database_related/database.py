from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base


engine = create_engine('sqlite:///library.db', echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

