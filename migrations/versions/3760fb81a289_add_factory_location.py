"""add factory location

Revision ID: 3760fb81a289
Revises: 1ec3ded43905
Create Date: 2019-09-06 16:10:05.944413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3760fb81a289'
down_revision = '1ec3ded43905'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('factory_location',
    sa.Column('factory_id', sa.BigInteger(), nullable=False),
    sa.Column('region_id', sa.Integer(), nullable=False),
    sa.Column('from_date_time', sa.DateTime(), nullable=True),
    sa.Column('until_date_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['factory_id'], ['factory.id'], name=op.f('fk_factory_location_factory_id_factory')),
    sa.ForeignKeyConstraint(['region_id'], ['region.id'], name=op.f('fk_factory_location_region_id_region')),
    sa.PrimaryKeyConstraint('factory_id', 'region_id', name=op.f('pk_factory_location'))
    )
    op.drop_constraint('fk_factory_stat_region_id_region', 'factory_stat', type_='foreignkey')
    op.drop_column('factory_stat', 'region_id')


def downgrade():
    op.add_column('factory_stat', sa.Column('region_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('fk_factory_stat_region_id_region', 'factory_stat', 'region', ['region_id'], ['id'])
    op.drop_table('factory_location')
