from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, database, models, schemas
from .database import SessionLocal, engine

database.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
