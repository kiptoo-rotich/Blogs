"""empty message

Revision ID: 24c14e79fc2d
Revises: c1005aab52af
Create Date: 2021-06-20 08:49:11.131306

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '24c14e79fc2d'
down_revision = 'c1005aab52af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blog_category', sa.String(length=255), nullable=True),
    sa.Column('blog_title', sa.String(length=255), nullable=True),
    sa.Column('blog_content', sa.String(length=255), nullable=True, min_length=100),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('shopping')
    op.drop_table('order')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('order_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('order_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('total_cost', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='order_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='order_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('shopping',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('order_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pizza_category', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('topping_category', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('cost', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], name='shopping_order_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='shopping_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='shopping_pkey')
    )
    op.drop_table('blog')
    # ### end Alembic commands ###