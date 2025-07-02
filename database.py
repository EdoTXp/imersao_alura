"""
Module description:
This module contains database-related functionality for the Ellis project.
It includes functions for creating and managing the database connection,
as well as defining the database schema.

Author: Your Name
Date: Current Date
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Caminho para o arquivo SQLite (pode ser ajustado conforme necessário)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'escola.db')}"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    Create a database session that will be reused throughout the request.
    Y1:0
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
