"""add total offers to player track

Revision ID: 594ad25dd1b7
Revises: 73c8363fb4ad
Create Date: 2019-09-09 15:58:31.463913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '594ad25dd1b7'
down_revision = '73c8363fb4ad'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('personal_market_stat', sa.Column('total_offers', sa.Integer(), nullable=True))


def downgrade():
    op.drop_column('personal_market_stat', 'total_offers')
