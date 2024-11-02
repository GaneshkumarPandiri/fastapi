"""add few columns to posts table

Revision ID: 3fa93054f123
Revises: 2acc127aa6f7
Create Date: 2024-11-02 14:25:46.141398

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3fa93054f123'
down_revision: Union[str, None] = '2acc127aa6f7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("published",sa.Boolean(),nullable=True, server_default='TRUE')
                           )
    op.add_column("posts", sa.Column("created_at",sa.TIMESTAMP(timezone=True),server_default=sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_column("posts","published")
    op.drop_column("posts","created_at")
    pass
