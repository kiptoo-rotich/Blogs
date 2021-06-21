"""empty message

Revision ID: 5571c4fdbb43
Revises: a0c5418ad187
Create Date: 2021-06-21 16:48:28.650569

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5571c4fdbb43'
down_revision = 'a0c5418ad187'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comments_user_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'blog', ['blog_id'], ['id'])
    op.drop_column('comments', 'user_id')
    op.drop_column('comments', 'posted')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('comments', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_user_id_fkey', 'comments', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###
