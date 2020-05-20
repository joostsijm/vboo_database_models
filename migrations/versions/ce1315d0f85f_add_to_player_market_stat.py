"""add_to_player_market_stat

Revision ID: ce1315d0f85f
Revises: d9b4e754a98e
Create Date: 2020-05-20 10:08:05.566036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce1315d0f85f'
down_revision = 'd9b4e754a98e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('player_market_stat', sa.Column('eight_average', sa.Integer(), nullable=True))
    op.add_column('player_market_stat', sa.Column('five_average', sa.Integer(), nullable=True))
    op.add_column('player_market_stat', sa.Column('four_average', sa.Integer(), nullable=True))
    op.add_column('player_market_stat', sa.Column('nine_average', sa.Integer(), nullable=True))
    op.add_column('player_market_stat', sa.Column('one_average', sa.Integer(), nullable=True))
    op.add_column('player_market_stat', sa.Column('seven_average', sa.Integer(), nullable=True))
    op.add_column('player_market_stat', sa.Column('six_average', sa.Integer(), nullable=True))
    op.add_column('player_market_stat', sa.Column('ten_average', sa.Integer(), nullable=True))
    op.add_column('player_market_stat', sa.Column('three_average', sa.Integer(), nullable=True))
    op.add_column('player_market_stat', sa.Column('two_average', sa.Integer(), nullable=True))
    op.drop_column('player_market_stat', 'one_t_average')
    op.drop_column('player_market_stat', 'five_t_average')
    op.drop_column('player_market_stat', 'two_t_average')
    op.drop_column('player_market_stat', 'half_t_average')


def downgrade():
    op.add_column('player_market_stat', sa.Column('half_t_average', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('player_market_stat', sa.Column('two_t_average', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('player_market_stat', sa.Column('five_t_average', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('player_market_stat', sa.Column('one_t_average', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('player_market_stat', 'two_average')
    op.drop_column('player_market_stat', 'three_average')
    op.drop_column('player_market_stat', 'ten_average')
    op.drop_column('player_market_stat', 'six_average')
    op.drop_column('player_market_stat', 'seven_average')
    op.drop_column('player_market_stat', 'one_average')
    op.drop_column('player_market_stat', 'nine_average')
    op.drop_column('player_market_stat', 'four_average')
    op.drop_column('player_market_stat', 'five_average')
    op.drop_column('player_market_stat', 'eight_average')
