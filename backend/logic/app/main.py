from fastapi import Depends, FastAPI, HTTPException, status
from database import engine
from tickets import models as tickets_models
from tickets import main as tickets_main


tickets_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tickets_main.router)


@app.get("/")
async def root():
    return {"message": "backend server is running"}
