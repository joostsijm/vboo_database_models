"""add region id to deep exploration orders

Revision ID: 95e16c281a76
Revises: 5081ca31d1c3
Create Date: 2020-02-13 09:54:29.287214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95e16c281a76'
down_revision = '5081ca31d1c3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('deep_exploration_order', sa.Column('region_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_deep_exploration_order_region_id_region'), 'deep_exploration_order', 'region', ['region_id'], ['id'])


def downgrade():
    op.drop_constraint(op.f('fk_deep_exploration_order_region_id_region'), 'deep_exploration_order', type_='foreignkey')
    op.drop_column('deep_exploration_order', 'region_id')
