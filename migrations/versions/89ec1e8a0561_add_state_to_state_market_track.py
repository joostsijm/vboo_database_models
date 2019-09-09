"""add state to state market track

Revision ID: 89ec1e8a0561
Revises: ce18c26cb4be
Create Date: 2019-09-09 13:35:27.216929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89ec1e8a0561'
down_revision = 'ce18c26cb4be'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('factory_location', 'factory_id',
               existing_type=sa.BIGINT(),
               type_=sa.Integer())
    op.add_column('state_market_stat', sa.Column('amount', sa.BigInteger(), nullable=True))
    op.add_column('state_market_stat', sa.Column('state_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_state_market_stat_state_id_state'), 'state_market_stat', 'state', ['state_id'], ['id'])


def downgrade():
    op.drop_constraint(op.f('fk_state_market_stat_state_id_state'), 'state_market_stat', type_='foreignkey')
    op.drop_column('state_market_stat', 'state_id')
    op.drop_column('state_market_stat', 'amount')
    op.alter_column('factory_location', 'factory_id',
               existing_type=sa.Integer(),
               type_=sa.BIGINT())
