from uuid import uuid4
from fastapi import status, File, UploadFile, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from dependencies import get_db
from typing import List
from . import crud
from . import models
from . import schemas


router = APIRouter(
    prefix="/api/users",
    tags=["Users"]
)


@router.get("/", response_model=List[schemas.User])
async def get_all_users(db: Session = Depends(get_db),):
    return await crud.get_all_users(db=db)

@router.post("/", response_model=schemas.User)
async def create_user(
    user: schemas.CreateUser,
    db: Session = Depends(get_db),
):
    return await crud.create_user(user=user, db=db)
