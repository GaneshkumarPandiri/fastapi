"""add new column 

Revision ID: 13b2d139fe58
Revises: bdee8ea21bc3
Create Date: 2024-11-02 13:57:26.723749

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '13b2d139fe58'
down_revision: Union[str, None] = 'bdee8ea21bc3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts","content")
    pass
