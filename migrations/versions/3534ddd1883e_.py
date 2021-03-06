"""empty message

Revision ID: 3534ddd1883e
Revises: 16dfd8a3dc41
Create Date: 2015-04-18 11:35:45.030636

"""

# revision identifiers, used by Alembic.
revision = '3534ddd1883e'
down_revision = '16dfd8a3dc41'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('userscore', sa.Column('question_id', sa.Integer(), nullable=True))
    op.add_column('userscore', sa.Column('user_username', sa.String(length=15), nullable=True))
    op.create_unique_constraint(None, 'userscore', ['id'])
    op.drop_constraint(u'userscore_user_fkey', 'userscore', type_='foreignkey')
    op.drop_constraint(u'userscore_question_fkey', 'userscore', type_='foreignkey')
    op.create_foreign_key(None, 'userscore', 'question', ['question_id'], ['id'])
    op.create_foreign_key(None, 'userscore', 'user', ['user_username'], ['username'])
    op.drop_column('userscore', 'question')
    op.drop_column('userscore', 'user')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('userscore', sa.Column('user', sa.VARCHAR(length=15), autoincrement=False, nullable=True))
    op.add_column('userscore', sa.Column('question', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'userscore', type_='foreignkey')
    op.drop_constraint(None, 'userscore', type_='foreignkey')
    op.create_foreign_key(u'userscore_question_fkey', 'userscore', 'question', ['question'], ['id'])
    op.create_foreign_key(u'userscore_user_fkey', 'userscore', 'user', ['user'], ['username'])
    op.drop_constraint(None, 'userscore', type_='unique')
    op.drop_column('userscore', 'user_username')
    op.drop_column('userscore', 'question_id')
    ### end Alembic commands ###
