"""add bloc

Revision ID: ae444ab1a42b
Revises: 95e16c281a76
Create Date: 2020-03-02 12:54:46.854784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae444ab1a42b'
down_revision = '95e16c281a76'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('bloc',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('state_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['state_id'], ['state.id'], name=op.f('fk_bloc_state_id_state')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_bloc'))
    )
    op.create_table('bloc_states',
    sa.Column('bloc_id', sa.Integer(), nullable=False),
    sa.Column('state_id', sa.Integer(), nullable=False),
    sa.Column('from_date_time', sa.DateTime(), nullable=False),
    sa.Column('until_date_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['bloc_id'], ['region.id'], name=op.f('fk_bloc_states_bloc_id_region')),
    sa.ForeignKeyConstraint(['state_id'], ['state.id'], name=op.f('fk_bloc_states_state_id_state')),
    sa.PrimaryKeyConstraint('bloc_id', 'state_id', 'from_date_time', name=op.f('pk_bloc_states'))
    )


def downgrade():
    op.drop_table('bloc_states')
    op.drop_table('bloc')
