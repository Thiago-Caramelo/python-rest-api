from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from ..database.database import SessionLocal
from ..database import schemas, crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/users/", tags=["users"], response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users
