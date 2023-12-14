from fastapi import status, File, UploadFile, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from dependencies import get_db
from typing import List
from . import crud
from . import models
from . import schemas


router = APIRouter(
    prefix="/tickets",
)


@router.get("/", response_model=List[schemas.Ticket])
async def get_all_tickets(db: Session = Depends(get_db),):
    return await crud.get_all_tickets(db=db)


@router.get("/{ticket_id}", response_model=schemas.Ticket)
async def get_ticket_by_id(
    ticket_id: int,
    db: Session = Depends(get_db)
):
    ticket = crud.get_ticket_by_id(ticket_id=ticket_id, db=db)
    if ticket is None:
        raise HTTPException(
            status_code=404, detail="Ticket not found")
    return ticket


@router.post("/", response_model=schemas.Ticket)
async def create_ticket(
    ticket: schemas.CreateTicket,
    db: Session = Depends(get_db),
):
    return await crud.create_ticket(ticket=ticket, db=db)


@router.put("/{ticket_id}", response_model=schemas.Ticket)
async def update_ticket(
    ticket_id: int,
    ticket_data: schemas.UpdateTicket,
    db: Session = Depends(get_db),
):
    ticket =  crud.get_ticket_by_id(db=db, ticket_id=ticket_id)
    if ticket is None:
        raise HTTPException(
            status_code=404, detail="Ticket does not exist")

    return await crud.update_ticket(
        ticket_data=ticket_data, ticket=ticket, db=db
    )
