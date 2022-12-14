"""empty message

Revision ID: 40757f41a42a
Revises: 739132786ff2
Create Date: 2022-11-30 22:22:40.245846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40757f41a42a'
down_revision = '739132786ff2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('period', sa.String(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('unit', sa.String(), nullable=True),
    sa.Column('subject', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('course')
    op.drop_table('student')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('phone_number', sa.VARCHAR(), nullable=True),
    sa.Column('birth_date', sa.DATE(), nullable=True),
    sa.Column('course_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('course',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('course_name', sa.VARCHAR(), nullable=True),
    sa.Column('course_duration', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('transactions')
    # ### end Alembic commands ###
