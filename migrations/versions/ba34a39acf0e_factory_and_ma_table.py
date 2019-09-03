"""factory and ma table

Revision ID: ba34a39acf0e
Revises: e6577173fe0f
Create Date: 2019-09-03 11:37:53.165412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba34a39acf0e'
down_revision = 'e6577173fe0f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('factory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], name=op.f('fk_factory_player_id_player')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_factory'))
    )
    op.create_table('factory_track',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=True),
    sa.Column('state_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['state_id'], ['state.id'], name=op.f('fk_factory_track_state_id_state')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_factory_track'))
    )
    op.create_table('military_academy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=True),
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('region_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], name=op.f('fk_military_academy_player_id_player')),
    sa.ForeignKeyConstraint(['region_id'], ['region.id'], name=op.f('fk_military_academy_region_id_region')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_military_academy'))
    )
    op.create_table('factory_stat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('level', sa.SmallInteger(), nullable=True),
    sa.Column('workers', sa.SmallInteger(), nullable=True),
    sa.Column('experience', sa.Integer(), nullable=True),
    sa.Column('wage', sa.Integer(), nullable=True),
    sa.Column('factory_id', sa.Integer(), nullable=True),
    sa.Column('factory_track_id', sa.Integer(), nullable=True),
    sa.Column('region_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['factory_id'], ['factory.id'], name=op.f('fk_factory_stat_factory_id_factory')),
    sa.ForeignKeyConstraint(['factory_track_id'], ['factory_track.id'], name=op.f('fk_factory_stat_factory_track_id_factory_track')),
    sa.ForeignKeyConstraint(['region_id'], ['region.id'], name=op.f('fk_factory_stat_region_id_region')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_factory_stat'))
    )


def downgrade():
    op.drop_table('factory_stat')
    op.drop_table('military_academy')
    op.drop_table('factory_track')
    op.drop_table('factory')
