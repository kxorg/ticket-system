from sqlalchemy.orm import Session
from . import models
from . import schemas

async def get_all_tickets(db: "Session") -> [schemas.Ticket]:
    tickets = db.query(models.Ticket).all()
    return [schemas.Ticket(**ticket.__dict__) for ticket in tickets]


def get_ticket_by_id(ticket_id: int, db: "Session") -> schemas.Ticket:
    ticket = db.query(models.Ticket).filter(
        models.Ticket.id == ticket_id).first()
    return ticket


async def create_ticket(ticket: schemas.Ticket, db: "Session") -> schemas.Ticket:
    ticket_model = models.Ticket(**ticket.dict())
    db.add(ticket_model)
    db.commit()
    db.refresh(ticket_model)
    return schemas.Ticket(**ticket_model.__dict__)


async def update_ticket(ticket_data: schemas.UpdateTicket, ticket: models.Ticket, db: "Session") -> schemas.Ticket:
    ticket.created_at = ticket_data.created_at

    db.commit()
    db.refresh(ticket)

    return schemas.Ticket.from_orm(ticket)
