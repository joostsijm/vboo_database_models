"""remove telegram verification

Revision ID: 9524fe8e91f0
Revises: 97d0cf5e4bb0
Create Date: 2020-02-11 00:03:26.671954

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9524fe8e91f0'
down_revision = '97d0cf5e4bb0'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('telegram_verification')


def downgrade():
    op.create_table('telegram_verification',
    sa.Column('player_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('telegram_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('code', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('date_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('confirmed', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], name='fk_telegram_verification_player_id_player'),
    sa.ForeignKeyConstraint(['telegram_id'], ['telegram_account.id'], name='fk_telegram_verification_telegram_id_telegram_account'),
    sa.PrimaryKeyConstraint('player_id', 'telegram_id', name='pk_telegram_verification')
    )
