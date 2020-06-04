from fastapi import Depends, FastAPI, Header, HTTPException
from .routers import users

app = FastAPI()

app.include_router(users.router)
