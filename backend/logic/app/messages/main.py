from fastapi import status, File, UploadFile, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from dependencies import get_db
from typing import List
from . import crud
from . import models
from . import schemas


router = APIRouter(
    prefix="/api/messages",
    tags=["Messages"]
)


@router.get("/", response_model=List[schemas.Message])
async def get_all_messages(db: Session = Depends(get_db),):
    return await crud.get_all_messages(db=db)

@router.post("/", response_model=schemas.Message)
async def create_message(
    message: schemas.CreateMessage,
    db: Session = Depends(get_db),
):
    return await crud.create_message(message=message, db=db)
