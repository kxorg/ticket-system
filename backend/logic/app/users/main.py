from datetime import timedelta
from uuid import uuid4
from fastapi import status, File, UploadFile, Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from dependencies import get_db
from typing import List
from . import crud
from . import models
from . import schemas
from . import settings


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

@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = crud.authenticate_user(form_data.name, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.create_access_token(
        data={"sub": user.name, "other_custom_data": [1, 2, 3, 4]},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")