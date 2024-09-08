from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the SQLite database using SQLAlchemy
DATABASE_URL = "sqlite:///tracker.db"

engine = create_engine(DATABASE_URL)

dbSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)

Session = dbSession()