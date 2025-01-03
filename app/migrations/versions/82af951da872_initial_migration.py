"""Initial migration

Revision ID: 82af951da872
Revises: 0525dccab68d
Create Date: 2025-01-03 12:17:38.429333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82af951da872'
down_revision = '0525dccab68d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('members')
    with op.batch_alter_table('member', schema=None) as batch_op:
        batch_op.drop_column('password_hash')
        batch_op.drop_column('role')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('member', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.VARCHAR(length=50), nullable=True))
        batch_op.add_column(sa.Column('password_hash', sa.VARCHAR(length=200), nullable=False))

    op.create_table('members',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('email', sa.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###
