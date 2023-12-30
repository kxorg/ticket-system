from fastapi import HTTPException
from pydantic import validator
from pydantic import BaseModel
import datetime as _dt
from uuid import UUID
import re

class _BaseUser(BaseModel):
    name: str


class User(_BaseUser):
    id: UUID
    created_at: _dt.datetime
    name: str
    hashed_password: str

    class Config:
        from_attributes = True


class CreateUser(_BaseUser):
    name: str
    password: str

    @validator("name")
    def validate_name(cls, value):
        LETTER_MATCH_PATTERN = re.compile(r"^[a-zA-Z\-]+$")
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Name should contains only letters (not digits!)"
            )
        return value
    

class TokenBase(BaseModel):
    access_token: str
    token_type: str

class TokenCreate(TokenBase):
    pass

class Token(TokenBase):
    id: int

    class Config:
        from_attributes = True
