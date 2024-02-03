from fastapi import FastAPI
from api import user_api
from db.base import Base, engine

app = FastAPI()

# Create database tables on startup
Base.metadata.create_all(bind=engine)

app.include_router(user_api.router, prefix="/user", tags=["user"])