from fastapi import FastAPI
from api import account_opening_api
from db import database as models 

models.Base.metadata.create_all(bind=models.engine)

app = FastAPI()

app.include_router(account_opening_api.router, prefix="/account", tags=["account"])