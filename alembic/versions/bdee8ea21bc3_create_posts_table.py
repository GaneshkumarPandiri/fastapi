"""create posts table

Revision ID: bdee8ea21bc3
Revises: 
Create Date: 2024-11-02 13:14:04.042239

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bdee8ea21bc3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("posts",sa.Column('id',sa.Integer(),nullable=False,primary_key=True),sa.Column('title',sa.String(),nullable=False))


def downgrade() -> None:
    op.drop_table("posts")
    pass
