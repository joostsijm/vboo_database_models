"""rename personal to player

Revision ID: 386c94d11473
Revises: 594ad25dd1b7
Create Date: 2019-09-09 17:39:59.800271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '386c94d11473'
down_revision = '594ad25dd1b7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('player_market_stat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_type', sa.SmallInteger(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('amount', sa.BigInteger(), nullable=True),
    sa.Column('total_offers', sa.Integer(), nullable=True),
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('market_track_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['market_track_id'], ['market_track.id'], name=op.f('fk_player_market_stat_market_track_id_market_track')),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], name=op.f('fk_player_market_stat_player_id_player')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_player_market_stat'))
    )
    op.drop_table('personal_market_stat')


def downgrade():
    op.create_table('personal_market_stat',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('item_type', sa.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('market_track_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('amount', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('player_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('total_offers', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['market_track_id'], ['market_track.id'], name='fk_personal_market_stat_market_track_id_market_track'),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], name='fk_personal_market_stat_player_id_player'),
    sa.PrimaryKeyConstraint('id', name='pk_personal_market_stat')
    )
    op.drop_table('player_market_stat')
