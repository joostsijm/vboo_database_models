"""Initial migration

Revision ID: 931dee70fc71
Revises: 
Create Date: 2019-08-21 17:19:36.721148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '931dee70fc71'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('region',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('gold_limit', sa.SmallInteger(), nullable=True),
    sa.Column('oil_limit', sa.SmallInteger(), nullable=True),
    sa.Column('ore_limit', sa.SmallInteger(), nullable=True),
    sa.Column('uranium_limit', sa.SmallInteger(), nullable=True),
    sa.Column('diamond_limit', sa.SmallInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_region'))
    )
    op.create_table('state',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_state'))
    )
    op.create_table('deep_exploration',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_time_end', sa.DateTime(), nullable=True),
    sa.Column('resource_type', sa.SmallInteger(), nullable=True),
    sa.Column('region_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['region_id'], ['region.id'], name=op.f('fk_deep_exploration_region_id_region')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_deep_exploration'))
    )
    op.create_table('resource_track',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resource_type', sa.SmallInteger(), nullable=True),
    sa.Column('date_time', sa.DateTime(), nullable=True),
    sa.Column('state_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['state_id'], ['state.id'], name=op.f('fk_resource_track_state_id_state')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_resource_track'))
    )
    op.create_table('resource_stat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('explored', sa.SmallInteger(), nullable=True),
    sa.Column('deep_exploration', sa.SmallInteger(), nullable=True),
    sa.Column('percentage_explored', sa.SmallInteger(), nullable=True),
    sa.Column('percentage_total', sa.SmallInteger(), nullable=True),
    sa.Column('resource_track_id', sa.Integer(), nullable=True),
    sa.Column('region_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['region_id'], ['region.id'], name=op.f('fk_resource_stat_region_id_region')),
    sa.ForeignKeyConstraint(['resource_track_id'], ['resource_track.id'], name=op.f('fk_resource_stat_resource_track_id_resource_track')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_resource_stat'))
    )


def downgrade():
    op.drop_table('resource_stat')
    op.drop_table('resource_track')
    op.drop_table('deep_exploration')
    op.drop_table('state')
    op.drop_table('region')
