from typing import List, Optional
from pydantic import BaseModel
import uuid


class UserSchema(BaseModel):
    id:  Optional[uuid.UUID] = None
    email: str
    is_active: bool

    class Config:
        orm_mode = True
