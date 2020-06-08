from typing import List
from pydantic import BaseModel
import uuid


class UserSchema(BaseModel):
    id: uuid.UUID
    email: str
    is_active: bool

    class Config:
        orm_mode = True
