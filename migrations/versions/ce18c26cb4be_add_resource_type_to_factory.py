"""add resource type to factory

Revision ID: ce18c26cb4be
Revises: 3760fb81a289
Create Date: 2019-09-08 20:45:05.776765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce18c26cb4be'
down_revision = '3760fb81a289'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('factory', sa.Column('resource_type', sa.SmallInteger(), nullable=True))


def downgrade():
    op.drop_column('factory', 'resource_type')
