"""  This module contains the main FastAPI application setup."""
from fastapi import FastAPI
from config.database import engine
from model import models
from routers import subscription
from rabbitmq.consumer import RabbitMQConsumer
from asyncio import create_task


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
rabbitmq = RabbitMQConsumer()

app.include_router(subscription.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.on_event("startup")
async def startup_event():
    create_task(rabbitmq.start_consuming())
