"""add state to department

Revision ID: 82a809b72bf3
Revises: 0c526a49471c
Create Date: 2019-09-03 15:07:27.138712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82a809b72bf3'
down_revision = '0c526a49471c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('department', sa.Column('state_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_department_state_id_state'), 'department', 'state', ['state_id'], ['id'])


def downgrade():
    op.drop_constraint(op.f('fk_department_state_id_state'), 'department', type_='foreignkey')
    op.drop_column('department', 'state_id')
