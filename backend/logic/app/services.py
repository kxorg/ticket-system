# import database as _database
# import models as _models
# import schemas as _schemas


# def get_db():
#     db = _database.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# async def get_all_tickets(db: "Session") -> List[_schemas.Ticket]:
#     tickets = db.query(_models.Ticket).all()
#     return [_schemas.Ticket(**ticket.__dict__) for ticket in tickets]


# def get_ticket_by_id(ticket_id: int, db: "Session") -> _schemas.Ticket:
#     ticket = db.query(_models.Ticket).filter(
#         _models.Ticket.id == ticket_id).first()
#     return ticket


# async def create_ticket(ticket: _schemas.Ticket, db: "Session") -> _schemas.Ticket:
#     ticket_model = _models.Ticket(**ticket.dict())
#     db.add(ticket_model)
#     db.commit()
#     db.refresh(ticket_model)
#     return _schemas.Ticket(**ticket_model.__dict__)


# async def update_ticket(ticket_data: _schemas.CreateTicket, ticket: _models.Ticket, db: "Session") -> _schemas.Ticket:
#     ticket.created_at = ticket_data.created_at

#     db.commit()
#     db.refresh(ticket)

#     return _schemas.Ticket.from_orm(ticket)
