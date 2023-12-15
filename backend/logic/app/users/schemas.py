import datetime as _dt
from pydantic import BaseModel
from uuid import UUID

class _BaseUser(BaseModel):
    name: str


class User(_BaseUser):
    id: UUID
    created_at: _dt.datetime
    name: str

    class Config:
        from_attributes = True


class CreateUser(_BaseUser):
    name: str
    # id: UUID