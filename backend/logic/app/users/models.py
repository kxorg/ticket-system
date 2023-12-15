from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, UUID
from sqlalchemy.orm import relationship
import datetime

from database import Base 


class User(Base):
    __tablename__ = "user"
    id = Column(UUID, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    name = Column(String, nullable=True)