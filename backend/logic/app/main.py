from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services
import database as _database

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()

_database.Base.metadata.create_all(bind=_database.engine)


@app.get("/")
async def root():
    return {"message": "backend server is running"}

@app.get("/api/tickets/", response_model=List[_schemas.Ticket])
async def get_tickets(
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return await _services.get_all_tickets(db=db)

@app.post("/api/tickets/", response_model=_schemas.Ticket)
async def create_contact(
    ticket: _schemas.CreateTicket,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return await _services.create_ticket(ticket=ticket, db=db)
