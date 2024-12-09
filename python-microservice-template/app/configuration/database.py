# app/configuration/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")

engine = create_engine(DATABASE_URL, echo=False, pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
