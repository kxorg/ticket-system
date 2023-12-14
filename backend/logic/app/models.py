import datetime as _dt
import sqlalchemy as _sql

import database as _database


class Ticket(_database.Base):
    __tablename__ = "tickets"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    created_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)