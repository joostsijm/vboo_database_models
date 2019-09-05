"""add work permit table

Revision ID: 6a81f102bb33
Revises: 96951df04b3b
Create Date: 2019-09-05 12:46:29.077779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a81f102bb33'
down_revision = '96951df04b3b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('state_work_permit',
    sa.Column('state_id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('from_date_time', sa.DateTime(), nullable=True),
    sa.Column('until_date_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], name=op.f('fk_state_work_permit_player_id_player')),
    sa.ForeignKeyConstraint(['state_id'], ['state.id'], name=op.f('fk_state_work_permit_state_id_state')),
    sa.PrimaryKeyConstraint('state_id', 'player_id', name=op.f('pk_state_work_permit'))
    )


def downgrade():
    op.drop_table('state_work_permit')
