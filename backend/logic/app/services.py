import time
from typing import TYPE_CHECKING, List

import database as _database
import models as _models
import schemas as _schemas

import logging
logger = logging.getLogger('gunicorn.error')

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()



async def get_all_tickets(db: "Session") -> List[_schemas.Ticket]:
    tickets = db.query(_models.Ticket).all()
    return [_schemas.Ticket(**ticket.__dict__) for ticket in tickets]

async def create_ticket(ticket: _schemas.Ticket, db: "Session") -> _schemas.Ticket:
    ticket_model = _models.Ticket(**ticket.dict())
    db.add(ticket_model)
    db.commit()
    db.refresh(ticket_model)
    return _schemas.Ticket(**ticket_model.__dict__)
