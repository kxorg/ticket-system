from uuid import uuid4
from sqlalchemy.orm import Session
from typing import Union
from . import models
from . import schemas
from hashing import Hasher
from dals import UserDAL

async def get_all_users(db: "Session") -> [schemas.User]:
    users = db.query(models.User).all()
    return [schemas.User(**user.__dict__) for user in users]


async def create_user(user: schemas.CreateUser, db: Session) -> schemas.User:
    hashed_password = Hasher.get_password_hash(user.password)
    user_model = models.User(name=user.name, hashed_password=hashed_password)
    user_id = uuid4()
    user_model.id = user_id
    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    return schemas.User(**user_model.__dict__)



def _get_user_by_name_for_auth(name: str, db: Session):
        user_dal = UserDAL(db)
        return user_dal.get_user_by_name(name=name)


async def authenticate_user(user: schemas.CreateUser, db: Session) -> Union[models.User, None]:
    user = _get_user_by_name_for_auth(name=user.name, db=db)
    if user is None:
        return
    if not Hasher.verify_password(user.password, user.hashed_password):
        return
    return user
