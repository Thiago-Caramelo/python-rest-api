from typing import List
from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    is_active: bool

    class Config:
        orm_mode = True
