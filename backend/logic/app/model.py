from sqlalchemy import Column, Integer, String
from config import Base

class Ticket(Base):
    __tablename__ = 'ticket'

    id=Column(Integer, primary_key=True)
    