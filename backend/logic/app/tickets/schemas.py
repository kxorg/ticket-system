import datetime as _dt
from pydantic import BaseModel


class _BaseTicket(BaseModel):
    pass


class Ticket(_BaseTicket):
    id: int
    created_at: _dt.datetime

    class Config:
        from_attributes = True


class CreateTicket(_BaseTicket):
    pass


class UpdateTicket(_BaseTicket):
    created_at: _dt.datetime
