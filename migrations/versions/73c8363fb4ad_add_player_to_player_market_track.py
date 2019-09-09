"""add player to player market track

Revision ID: 73c8363fb4ad
Revises: 89ec1e8a0561
Create Date: 2019-09-09 15:45:15.429371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73c8363fb4ad'
down_revision = '89ec1e8a0561'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('personal_market_stat', sa.Column('amount', sa.BigInteger(), nullable=True))
    op.add_column('personal_market_stat', sa.Column('player_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_personal_market_stat_player_id_player'), 'personal_market_stat', 'player', ['player_id'], ['id'])


def downgrade():
    op.drop_constraint(op.f('fk_personal_market_stat_player_id_player'), 'personal_market_stat', type_='foreignkey')
    op.drop_column('personal_market_stat', 'player_id')
    op.drop_column('personal_market_stat', 'amount')
