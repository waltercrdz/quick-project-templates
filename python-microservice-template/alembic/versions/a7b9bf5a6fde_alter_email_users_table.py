"""alter email users table

Revision ID: a7b9bf5a6fde
Revises: 8f0e9c01e9a2
Create Date: 2024-10-25 21:10:02.974636

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy


# revision identifiers, used by Alembic.
revision: str = "a7b9bf5a6fde"
down_revision: Union[str, None] = "8f0e9c01e9a2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column("users", "email", type_=sqlalchemy.String(30))


def downgrade() -> None:
    pass
