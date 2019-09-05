"""fix player id to biginteger

Revision ID: 1ec3ded43905
Revises: f058537a8871
Create Date: 2019-09-05 15:54:03.864675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ec3ded43905'
down_revision = 'f058537a8871'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('state_work_permit', 'player_id',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger())


def downgrade():
    op.alter_column('state_work_permit', 'player_id',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER())
