"""empty message

Revision ID: 5a65de9c389b
Revises: 53e3cd6bf15b
Create Date: 2021-06-20 23:30:00.128251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a65de9c389b'
down_revision = '53e3cd6bf15b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comment_data', sa.String(length=255), nullable=True))
    op.drop_column('comments', 'comment')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comment', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('comments', 'comment_data')
    # ### end Alembic commands ###