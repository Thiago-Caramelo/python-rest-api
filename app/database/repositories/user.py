from sqlalchemy.orm import Session
from app.database.models.user import User
from app.schemas.user import UserSchema
from uuid import UUID


def get_user(db: Session, user_id: UUID):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserSchema):
    db_user = User(email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
