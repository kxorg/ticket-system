import datetime as _dt
import pydantic as _pydantic

class _BaseTicket(_pydantic.BaseModel):
    pass


class Ticket(_BaseTicket):
    id: int
    created_at: _dt.datetime

    class Config:
        orm_mode = True
        from_attributes=True


class CreateTicket(_BaseTicket):
    pass

class UpdateTicket(_BaseTicket):
    created_at: _dt.datetime