"""create user and goal table

Revision ID: a76342f1d4c3
Revises: 95a8506ed336
Create Date: 2023-10-28 23:22:11.944210

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
# from sqlalchemy.dialects import mysql


# revision identifiers, used by Alembic.
revision: str = 'a76342f1d4c3'
down_revision: Union[str, None] = '95a8506ed336'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER, autoincrement=True, nullable=False),
    sa.Column('username', sa.String(80), nullable=False),
    sa.Column('password', sa.String(120), nullable=False),
    sa.Column('role', sa.String(80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('goals',
    sa.Column('id', sa.INTEGER, autoincrement=True, nullable=False),
    sa.Column('name', sa.String(120), nullable=False),
    sa.Column('target', sa.INTEGER, autoincrement=False, nullable=False),
    sa.Column('start_date', sa.String(120), nullable=False),
    sa.Column('end_date', sa.String(120), nullable=False),
    sa.Column('progress', sa.Float, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    pass
