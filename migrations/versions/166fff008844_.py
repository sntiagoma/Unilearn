"""empty message

Revision ID: 166fff008844
Revises: 346191f20b68
Create Date: 2015-03-18 18:37:39.207985

"""

# revision identifiers, used by Alembic.
revision = '166fff008844'
down_revision = '346191f20b68'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question_smm',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['question_model.cod'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question_completation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['question_model.cod'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(None, 'topic', ['name'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'topic', type_='unique')
    op.drop_table('question_completation')
    op.drop_table('question_smm')
    ### end Alembic commands ###