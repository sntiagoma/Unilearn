"""empty message

Revision ID: 2fd8a204a1b
Revises: 3b0e4ebb0003
Create Date: 2015-03-23 23:44:52.204382

"""

# revision identifiers, used by Alembic.
revision = '2fd8a204a1b'
down_revision = '3b0e4ebb0003'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'answer', ['id'])
    op.create_unique_constraint(None, 'question', ['id'])
    op.create_unique_constraint(None, 'topic', ['id'])
    op.create_unique_constraint(None, 'user', ['username'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'topic', type_='unique')
    op.drop_constraint(None, 'question', type_='unique')
    op.drop_constraint(None, 'answer', type_='unique')
    ### end Alembic commands ###
