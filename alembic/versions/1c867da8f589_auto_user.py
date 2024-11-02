"""auto user

Revision ID: 1c867da8f589
Revises: 8a00646044cb
Create Date: 2024-11-02 14:45:17.117547

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c867da8f589'
down_revision: Union[str, None] = '8a00646044cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'phone_number',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'phone_number',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    # ### end Alembic commands ###
