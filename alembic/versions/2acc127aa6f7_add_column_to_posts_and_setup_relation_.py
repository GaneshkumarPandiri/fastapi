"""add column to posts and setup relation ship

Revision ID: 2acc127aa6f7
Revises: 12e14e840d22
Create Date: 2024-11-02 14:19:19.539427

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2acc127aa6f7'
down_revision: Union[str, None] = '12e14e840d22'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("owner_id",sa.Integer(),nullable=False))
    op.create_foreign_key("post_users_fk",source_table="posts",referent_table="users",local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk",table_name="posts")
    op.drop_column("posts","user_id")
    pass
