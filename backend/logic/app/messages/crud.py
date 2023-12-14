from sqlalchemy.orm import Session
from . import models
from . import schemas


async def get_all_messages(db: "Session") -> [schemas.Message]:
    messages = db.query(models.Message).all()
    return [schemas.Message(**message.__dict__) for message in messages]


async def create_message(message: schemas.Message, db: "Session") -> schemas.Message:
    message_model = models.Message(**message.dict())
    db.add(message_model)
    db.commit()
    db.refresh(message_model)
    return schemas.Message(**message_model.__dict__)
