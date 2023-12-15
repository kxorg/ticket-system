from uuid import uuid4
from sqlalchemy.orm import Session
from . import models
from . import schemas


async def get_all_users(db: "Session") -> [schemas.User]:
    users = db.query(models.User).all()
    return [schemas.User(**user.__dict__) for user in users]


async def create_user(user: schemas.User, db: "Session") -> schemas.User:
    user_model = models.User(**user.dict())
    user_id = uuid4()
    user_model.id = user_id
    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    return schemas.User(**user_model.__dict__)
