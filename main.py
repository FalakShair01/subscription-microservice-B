"""  This module contains the main FastAPI application setup."""
from fastapi import FastAPI
from config.database import engine
from model import models
from routers import subscription


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(subscription.router)

@app.get("/")
async def root():
    """Welcome Message"""
    return {"message": "Hello World"}
