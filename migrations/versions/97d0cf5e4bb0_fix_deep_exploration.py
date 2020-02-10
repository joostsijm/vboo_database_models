"""fix_deep_exploration

Revision ID: 97d0cf5e4bb0
Revises: 75b3282b1d3f
Create Date: 2020-02-11 00:02:01.244499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97d0cf5e4bb0'
down_revision = '75b3282b1d3f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('deep_exploration', sa.Column('points', sa.Integer(), nullable=True))


def downgrade():
    op.drop_column('deep_exploration', 'points')
