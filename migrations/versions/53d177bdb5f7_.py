"""empty message

Revision ID: 53d177bdb5f7
Revises: 1105e8092b71
Create Date: 2015-06-01 09:28:16.208000

"""

# revision identifiers, used by Alembic.
revision = '53d177bdb5f7'
down_revision = '1105e8092b71'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'tw_username')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('tw_username', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    ### end Alembic commands ###
