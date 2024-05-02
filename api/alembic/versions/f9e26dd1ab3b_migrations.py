"""migrations

Revision ID: f9e26dd1ab3b
Revises: c12210d2fc1c
Create Date: 2024-04-30 21:13:30.691400

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f9e26dd1ab3b'
down_revision: Union[str, None] = 'c12210d2fc1c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
