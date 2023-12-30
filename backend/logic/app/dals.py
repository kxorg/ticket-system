from typing import Union
from uuid import UUID

from sqlalchemy import and_
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.orm import Session

from users.models import User

class UserDAL:

    def __init__(self, db: Session):
        self.db = db

    async def get_user_by_name(self, name: str) -> Union[User, None]:
        query = select(User).where(User.name == name)
        res = self.db.execute(query)
        user_row = res.fetchone()
        if user_row is not None:
            return user_row[0]