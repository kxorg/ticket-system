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
async def get_all_tickets(db: _orm.Session = _fastapi.Depends(_services.get_db),):
    return await _services.get_all_tickets(db=db)


@app.get("/api/tickets/{ticket_id}", response_model=_schemas.Ticket)
async def get_ticket_by_id(
    ticket_id: int,
    db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    ticket = _services.get_ticket_by_id(ticket_id=ticket_id, db=db)
    if ticket is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="Ticket not found")
    return ticket


@app.post("/api/tickets/", response_model=_schemas.Ticket)
async def create_ticket(
    ticket: _schemas.CreateTicket,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return await _services.create_ticket(ticket=ticket, db=db)

@app.put("/api/tickets/{ticket_id}", response_model=_schemas.Ticket)
async def update_ticket(
    ticket_id: int,
    ticket_data: _schemas.UpdateTicket,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    ticket = _services.get_ticket_by_id(db=db, ticket_id=ticket_id)
    if ticket is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="Ticket does not exist")

    return await _services.update_ticket(
        ticket_data=ticket_data, ticket=ticket, db=db
    )
