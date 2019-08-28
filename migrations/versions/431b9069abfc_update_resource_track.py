"""update_resource_track

Revision ID: 431b9069abfc
Revises: 931dee70fc71
Create Date: 2019-08-21 17:46:47.853150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '431b9069abfc'
down_revision = '931dee70fc71'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('resource_stat', sa.Column('limit_left', sa.SmallInteger(), nullable=True))
    op.drop_column('resource_stat', 'percentage_total')
    op.drop_column('resource_stat', 'percentage_explored')


def downgrade():
    op.add_column('resource_stat', sa.Column('percentage_explored', sa.SMALLINT(), autoincrement=False, nullable=True))
    op.add_column('resource_stat', sa.Column('percentage_total', sa.SMALLINT(), autoincrement=False, nullable=True))
    op.drop_column('resource_stat', 'limit_left')
