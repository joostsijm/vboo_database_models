"""update player join tables

Revision ID: a5cc743d9119
Revises: ba34a39acf0e
Create Date: 2019-09-03 11:42:13.438545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5cc743d9119'
down_revision = 'ba34a39acf0e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('election_stat', sa.Column('party_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_election_stat_party_id_party'), 'election_stat', 'party', ['party_id'], ['id'])
    op.add_column('player_location', sa.Column('from_date_time', sa.DateTime(), nullable=True))
    op.add_column('player_location', sa.Column('until_date_time', sa.DateTime(), nullable=True))
    op.add_column('player_party', sa.Column('from_date_time', sa.DateTime(), nullable=True))
    op.add_column('player_party', sa.Column('until_date_time', sa.DateTime(), nullable=True))
    op.add_column('player_residency', sa.Column('from_date_time', sa.DateTime(), nullable=True))
    op.add_column('player_residency', sa.Column('until_date_time', sa.DateTime(), nullable=True))


def downgrade():
    op.drop_column('player_residency', 'until_date_time')
    op.drop_column('player_residency', 'from_date_time')
    op.drop_column('player_party', 'until_date_time')
    op.drop_column('player_party', 'from_date_time')
    op.drop_column('player_location', 'until_date_time')
    op.drop_column('player_location', 'from_date_time')
    op.drop_constraint(op.f('fk_election_stat_party_id_party'), 'election_stat', type_='foreignkey')
    op.drop_column('election_stat', 'party_id')
