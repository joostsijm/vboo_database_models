"""add registration date to play

Revision ID: f058537a8871
Revises: 6a81f102bb33
Create Date: 2019-09-05 13:52:42.319013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f058537a8871'
down_revision = '6a81f102bb33'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('player', sa.Column('registration_date', sa.Date(), nullable=True))


def downgrade():
    op.drop_column('player', 'registration_date')
