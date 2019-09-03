"""add date to state region

Revision ID: 42df131326b1
Revises: 1547a089e232
Create Date: 2019-09-03 12:13:45.719175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42df131326b1'
down_revision = '1547a089e232'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('state_region', sa.Column('from_date_time', sa.DateTime(), nullable=True))
    op.add_column('state_region', sa.Column('until_date_time', sa.DateTime(), nullable=True))


def downgrade():
    op.drop_column('state_region', 'until_date_time')
    op.drop_column('state_region', 'from_date_time')
