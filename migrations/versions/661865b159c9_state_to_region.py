"""state_to_region

Revision ID: 661865b159c9
Revises: 376b13137050
Create Date: 2019-10-17 23:11:16.074823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '661865b159c9'
down_revision = '376b13137050'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('state_market_stat', sa.Column('region_id', sa.Integer(), nullable=True))
    op.drop_constraint('fk_state_market_stat_state_id_state', 'state_market_stat', type_='foreignkey')
    op.create_foreign_key(op.f('fk_state_market_stat_region_id_region'), 'state_market_stat', 'region', ['region_id'], ['id'])
    op.drop_column('state_market_stat', 'state_id')


def downgrade():
    op.add_column('state_market_stat', sa.Column('state_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(op.f('fk_state_market_stat_region_id_region'), 'state_market_stat', type_='foreignkey')
    op.create_foreign_key('fk_state_market_stat_state_id_state', 'state_market_stat', 'state', ['state_id'], ['id'])
    op.drop_column('state_market_stat', 'region_id')
