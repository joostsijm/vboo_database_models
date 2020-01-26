"""add_telegram_account

Revision ID: 75b3282b1d3f
Revises: 661865b159c9
Create Date: 2020-01-26 15:17:12.904010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75b3282b1d3f'
down_revision = '661865b159c9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('telegram_account',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('registration_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_telegram_account'))
    )
    op.create_table('player_telegram',
    sa.Column('player_id', sa.BigInteger(), nullable=False),
    sa.Column('telegram_id', sa.BigInteger(), nullable=False),
    sa.Column('from_date_time', sa.DateTime(), nullable=False),
    sa.Column('until_date_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], name=op.f('fk_player_telegram_player_id_player')),
    sa.ForeignKeyConstraint(['telegram_id'], ['telegram_account.id'], name=op.f('fk_player_telegram_telegram_id_telegram_account')),
    sa.PrimaryKeyConstraint('player_id', 'telegram_id', 'from_date_time', name=op.f('pk_player_telegram'))
    )
    op.create_table('telegram_handle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('handle', sa.String(), nullable=True),
    sa.Column('registration_date', sa.DateTime(), nullable=True),
    sa.Column('telegram_account_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['telegram_account_id'], ['telegram_account.id'], name=op.f('fk_telegram_handle_telegram_account_id_telegram_account')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_telegram_handle'))
    )
    op.create_table('telegram_verification',
    sa.Column('player_id', sa.BigInteger(), nullable=False),
    sa.Column('telegram_id', sa.BigInteger(), nullable=False),
    sa.Column('code', sa.String(), nullable=True),
    sa.Column('date_time', sa.DateTime(), nullable=True),
    sa.Column('confirmed', sa.Boolean(), server_default='f', nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], name=op.f('fk_telegram_verification_player_id_player')),
    sa.ForeignKeyConstraint(['telegram_id'], ['telegram_account.id'], name=op.f('fk_telegram_verification_telegram_id_telegram_account')),
    sa.PrimaryKeyConstraint('player_id', 'telegram_id', name=op.f('pk_telegram_verification'))
    )


def downgrade():
    op.drop_table('telegram_verification')
    op.drop_table('telegram_handle')
    op.drop_table('player_telegram')
    op.drop_table('telegram_account')
