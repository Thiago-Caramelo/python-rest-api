import app.database.session as session
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.database.repositories import user
from app.schemas.user import UserSchema
router = APIRouter()


@router.get("/users/", tags=["users"], response_model=List[UserSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(session.get_db)):
    users = user.get_users(db, skip=skip, limit=limit)
    return users
