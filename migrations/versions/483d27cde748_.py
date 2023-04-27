"""empty message

Revision ID: 483d27cde748
Revises: 3fc700762d8b
Create Date: 2023-04-27 14:59:08.715651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '483d27cde748'
down_revision = '3fc700762d8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('caption', sa.String(length=125), nullable=True),
    sa.Column('photo', sa.String(length=125), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Posts')
    # ### end Alembic commands ###
