"""empty message

Revision ID: dc339d16cfcc
Revises: 
Create Date: 2023-04-02 16:09:22.343291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc339d16cfcc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task_record',
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('spend_time', sa.Float(), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('finish_time', sa.DateTime(), nullable=True),
    sa.Column('data_rows', sa.Integer(), nullable=True),
    sa.Column('success', sa.Integer(), nullable=True),
    sa.Column('workers', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('task_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task_record')
    # ### end Alembic commands ###
