from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config import settings

engine = create_engine(settings.pg_dsn)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)