from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")
MYSQL_PORT = os.getenv("MYSQL_PORT")

DATABASE_URL = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@"
    f"{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the base class for the models
Base = declarative_base()


def get_db():
    """Provides a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
