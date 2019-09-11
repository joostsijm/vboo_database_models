"""fix player id to big integer

Revision ID: 0f35d62c414a
Revises: 386c94d11473
Create Date: 2019-09-10 21:43:24.524417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f35d62c414a'
down_revision = '386c94d11473'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('player_market_stat', 'player_id',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=True)


def downgrade():
    op.alter_column('player_market_stat', 'player_id',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               existing_nullable=True)
