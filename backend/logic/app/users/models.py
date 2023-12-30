from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, UUID
from sqlalchemy.orm import relationship
import datetime

from database import Base 


class User(Base):
    __tablename__ = "user"
    id = Column(UUID, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

class Token(Base):
    __tablename__ = "token"
    id = Column(Integer, primary_key=True, index=True)
    access_token = Column(String, nullable=False)
    token_type = Column(String, nullable=False)