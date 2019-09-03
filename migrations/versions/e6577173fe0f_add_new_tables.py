"""add new tables

Revision ID: e6577173fe0f
Revises: 431b9069abfc
Create Date: 2019-09-03 10:38:14.530991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6577173fe0f'
down_revision = '431b9069abfc'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('department_type', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_department'))
    )
    op.create_table('party',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(length=512), nullable=True),
    sa.Column('from_date_time', sa.DateTime(), nullable=True),
    sa.Column('until_date_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_party'))
    )
    op.create_table('player',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('nation', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_player'))
    )
    op.create_table('department_stat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=True),
    sa.Column('points', sa.SmallInteger(), nullable=True),
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['department.id'], name=op.f('fk_department_stat_department_id_department')),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], name=op.f('fk_department_stat_player_id_player')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_department_stat'))
    )
    op.create_table('election',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('state_id', sa.Integer(), nullable=True),
    sa.Column('convocation_date_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['state_id'], ['state.id'], name=op.f('fk_election_state_id_state')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_election'))
    )
    op.create_table('player_location',
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('region_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], name=op.f('fk_player_location_player_id_player')),
    sa.ForeignKeyConstraint(['region_id'], ['region.id'], name=op.f('fk_player_location_region_id_region'))
    )
    op.create_table('player_party',
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('party_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['party_id'], ['party.id'], name=op.f('fk_player_party_party_id_party')),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], name=op.f('fk_player_party_player_id_player'))
    )
    op.create_table('player_residency',
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('region_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], name=op.f('fk_player_residency_player_id_player')),
    sa.ForeignKeyConstraint(['region_id'], ['region.id'], name=op.f('fk_player_residency_region_id_region'))
    )
    op.create_table('state_region',
    sa.Column('state_id', sa.Integer(), nullable=True),
    sa.Column('region_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['region_id'], ['region.id'], name=op.f('fk_state_region_region_id_region')),
    sa.ForeignKeyConstraint(['state_id'], ['state.id'], name=op.f('fk_state_region_state_id_state'))
    )
    op.create_table('election_stat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('percentage', sa.SmallInteger(), nullable=True),
    sa.Column('seats', sa.SmallInteger(), nullable=True),
    sa.Column('election_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['election_id'], ['election.id'], name=op.f('fk_election_stat_election_id_election')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_election_stat'))
    )


def downgrade():
    op.drop_table('election_stat')
    op.drop_table('state_region')
    op.drop_table('player_residency')
    op.drop_table('player_party')
    op.drop_table('player_location')
    op.drop_table('election')
    op.drop_table('department_stat')
    op.drop_table('player')
    op.drop_table('party')
    op.drop_table('department')
