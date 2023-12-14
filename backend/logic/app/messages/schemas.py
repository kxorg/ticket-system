import datetime as _dt
from pydantic import BaseModel


class _BaseMessage(BaseModel):
    content: str


class Message(_BaseMessage):
    id: int
    created_at: _dt.datetime
    content: str

    class Config:
        from_attributes = True


class CreateMessage(_BaseMessage):
    content: str