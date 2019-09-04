"""player id to biginteger

Revision ID: 96951df04b3b
Revises: 82a809b72bf3
Create Date: 2019-09-04 13:09:22.495778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96951df04b3b'
down_revision = '82a809b72bf3'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('department_stat', 'player_id',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=True)
    op.alter_column('factory', 'player_id',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=True)
    op.alter_column('military_academy', 'player_id',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=True)
    op.alter_column('player', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               autoincrement=True,
               existing_server_default=sa.text("nextval('player_id_seq'::regclass)"))
    op.alter_column('player_location', 'player_id',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=True)
    op.alter_column('player_party', 'player_id',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=True)
    op.alter_column('player_residency', 'player_id',
               existing_type=sa.INTEGER(),
               type_=sa.BigInteger(),
               existing_nullable=True)


def downgrade():
    op.alter_column('player_residency', 'player_id',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.alter_column('player_party', 'player_id',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.alter_column('player_location', 'player_id',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.alter_column('player', 'id',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               autoincrement=True,
               existing_server_default=sa.text("nextval('player_id_seq'::regclass)"))
    op.alter_column('military_academy', 'player_id',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.alter_column('factory', 'player_id',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.alter_column('department_stat', 'player_id',
               existing_type=sa.BigInteger(),
               type_=sa.INTEGER(),
               existing_nullable=True)
