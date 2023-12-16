"""message

Revision ID: 373a2cb89f76
Revises: 1396b5518039
Create Date: 2023-12-16 01:09:31.714337

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '373a2cb89f76'
down_revision: Union[str, None] = '1396b5518039'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
