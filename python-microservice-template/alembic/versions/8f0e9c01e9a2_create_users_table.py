"""create users table

Revision ID: 8f0e9c01e9a2
Revises:
Create Date: 2024-10-25 20:52:21.979887

"""

from typing import Sequence, Union
import uuid

from alembic import op
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision: str = "8f0e9c01e9a2"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        Column(
            "id",
            UUID(as_uuid=True),
            primary_key=True,
            default=uuid.uuid4,
            unique=True,
            nullable=False,
        ),
        Column("email", String(30), nullable=False),
        Column("password", String, nullable=False),
    )


def downgrade() -> None:
    pass
