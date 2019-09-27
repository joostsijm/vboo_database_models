"""add average to market stat

Revision ID: 66117b73b1e6
Revises: 0f35d62c414a
Create Date: 2019-09-14 16:35:55.133887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66117b73b1e6'
down_revision = '0f35d62c414a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('player_market_stat', sa.Column('five_t_average', sa.Integer(), nullable=True))
    op.add_column('player_market_stat', sa.Column('half_t_average', sa.Integer(), nullable=True))
    op.add_column('player_market_stat', sa.Column('one_t_average', sa.Integer(), nullable=True))
    op.add_column('player_market_stat', sa.Column('two_t_average', sa.Integer(), nullable=True))


def downgrade():
    op.drop_column('player_market_stat', 'two_t_average')
    op.drop_column('player_market_stat', 'one_t_average')
    op.drop_column('player_market_stat', 'half_t_average')
    op.drop_column('player_market_stat', 'five_t_average')
