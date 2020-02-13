"""add deep exploration orders

Revision ID: 7976912082a6
Revises: 9524fe8e91f0
Create Date: 2020-02-11 13:13:53.215765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7976912082a6'
down_revision = '9524fe8e91f0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('deep_exploration_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resource_type', sa.SmallInteger(), nullable=False),
    sa.Column('order_type', sa.SmallInteger(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('from_date_time', sa.DateTime(), nullable=True),
    sa.Column('until_date_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_deep_exploration_order'))
    )


def downgrade():
    op.drop_table('deep_exploration_order')
