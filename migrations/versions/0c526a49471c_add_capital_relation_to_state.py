"""add capital relation to state

Revision ID: 0c526a49471c
Revises: 42df131326b1
Create Date: 2019-09-03 14:41:52.724530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c526a49471c'
down_revision = '42df131326b1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('state', sa.Column('capital_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_state_capital_id_region'), 'state', 'region', ['capital_id'], ['id'])


def downgrade():
    op.drop_constraint(op.f('fk_state_capital_id_region'), 'state', type_='foreignkey')
    op.drop_column('state', 'capital_id')
