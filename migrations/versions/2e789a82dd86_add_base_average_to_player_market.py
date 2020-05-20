"""add_base_average_to_player_market

Revision ID: 2e789a82dd86
Revises: ce1315d0f85f
Create Date: 2020-05-20 11:11:41.606325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e789a82dd86'
down_revision = 'ce1315d0f85f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('player_market_stat', sa.Column('base_average', sa.BigInteger(), nullable=True))


def downgrade():
    op.drop_column('player_market_stat', 'base_average')
