"""added new table users

Revision ID: 12e14e840d22
Revises: 13b2d139fe58
Create Date: 2024-11-02 14:07:50.299261

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '12e14e840d22'
down_revision: Union[str, None] = '13b2d139fe58'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users",sa.Column("id",sa.Integer(),nullable=False),
                            sa.Column("email",sa.String(),nullable=False),
                            sa.Column("password",sa.String(),nullable=False),
                            sa.Column("created_at",sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),
                            sa.PrimaryKeyConstraint("id"),
                            sa.UniqueConstraint("email")
                    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
