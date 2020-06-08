import app.database.session as session
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.database.repositories import user
from app.schemas.user import UserSchema
from uuid import UUID
router = APIRouter()


@router.get("/users/", tags=["users"], response_model=List[UserSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(session.get_db)):
    users = user.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", tags=["users"], response_model=UserSchema)
def read_user(user_id: UUID, db: Session = Depends(session.get_db)):
    db_user = user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/", tags=["users"], response_model=UserSchema)
def create_user(newUser: UserSchema, db: Session = Depends(session.get_db)):
    db_user = user.get_user_by_email(db, email=newUser.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user.create_user(db=db, user=newUser)
