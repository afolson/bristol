"""empty message

Revision ID: 111807b6e0d
Revises: 126a588b784
Create Date: 2014-04-12 09:54:24.691713

"""

# revision identifiers, used by Alembic.
revision = '111807b6e0d'
down_revision = '126a588b784'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('poop', sa.Column('rating', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('poop', 'rating')
    ### end Alembic commands ###
