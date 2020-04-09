"""change wp primary key

Revision ID: d9b4e754a98e
Revises: 95e16c281a76
Create Date: 2020-04-09 17:45:28.103910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9b4e754a98e'
down_revision = '95e16c281a76'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('pk_state_work_permit', 'state_work_permit', type_='primary')
    op.create_primary_key('pk_state_work_permit', 'state_work_permit', ['state_id', 'player_id', 'from_date_time'])


def downgrade():
    op.drop_constraint('pk_state_work_permit', 'state_work_permit', type_='primary')
    op.create_primary_key('pk_state_work_permit', 'state_work_permit', ['state_id', 'player_id'])
