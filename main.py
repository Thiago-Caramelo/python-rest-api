import uvicorn
from fastapi import Depends, FastAPI, Header, HTTPException
from app.routers import users
from app.database import models
from app.database.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)