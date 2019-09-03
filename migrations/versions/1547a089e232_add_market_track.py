"""add market track

Revision ID: 1547a089e232
Revises: a5cc743d9119
Create Date: 2019-09-03 12:02:55.635717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1547a089e232'
down_revision = 'a5cc743d9119'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('market_track',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_market_track'))
    )
    op.create_table('personal_market_stat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_type', sa.SmallInteger(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('market_track_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['market_track_id'], ['market_track.id'], name=op.f('fk_personal_market_stat_market_track_id_market_track')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_personal_market_stat'))
    )
    op.create_table('state_market_stat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_type', sa.SmallInteger(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('market_track_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['market_track_id'], ['market_track.id'], name=op.f('fk_state_market_stat_market_track_id_market_track')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_state_market_stat'))
    )


def downgrade():
    op.drop_table('state_market_stat')
    op.drop_table('personal_market_stat')
    op.drop_table('market_track')
