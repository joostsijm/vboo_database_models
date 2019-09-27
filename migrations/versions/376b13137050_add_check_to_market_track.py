"""add check to market track

Revision ID: 376b13137050
Revises: 66117b73b1e6
Create Date: 2019-09-15 18:15:31.976895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '376b13137050'
down_revision = '66117b73b1e6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('market_track', sa.Column('items', sa.Boolean(), server_default='f', nullable=True))
    op.add_column('market_track', sa.Column('player_resources', sa.Boolean(), server_default='f', nullable=True))
    op.add_column('market_track', sa.Column('state_resources', sa.Boolean(), server_default='f', nullable=True))


def downgrade():
    op.drop_column('market_track', 'state_resources')
    op.drop_column('market_track', 'player_resources')
    op.drop_column('market_track', 'items')
