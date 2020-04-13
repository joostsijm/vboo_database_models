"""rename deep exploration date column

Revision ID: 5081ca31d1c3
Revises: 7976912082a6
Create Date: 2020-02-11 22:51:56.652667

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5081ca31d1c3'
down_revision = '7976912082a6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('deep_exploration', sa.Column('until_date_time', sa.DateTime(), nullable=True))
    op.drop_column('deep_exploration', 'date_time_end')


def downgrade():
    op.add_column('deep_exploration', sa.Column('date_time_end', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('deep_exploration', 'until_date_time')
