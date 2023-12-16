"""<message>

Revision ID: f6d9a209aadf
Revises: 373a2cb89f76
Create Date: 2023-12-15 22:10:16.513884

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6d9a209aadf'
down_revision: Union[str, None] = '373a2cb89f76'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
