"""empty message

Revision ID: 11ed6e85f3b0
Revises: 
Create Date: 2023-01-03 19:29:41.117497

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '11ed6e85f3b0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('email')
        batch_op.drop_index('username')

    op.drop_table('users')
    op.drop_table('flask_dance_oauth')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flask_dance_oauth',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('provider', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=False),
    sa.Column('token', mysql.LONGTEXT(charset='utf8mb4', collation='utf8mb4_bin'), nullable=False),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='flask_dance_oauth_ibfk_1', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('users',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('password', sa.BLOB(), nullable=True),
    sa.Column('oauth_github', mysql.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index('username', ['username'], unique=False)
        batch_op.create_index('email', ['email'], unique=False)

    op.drop_table('product')
    # ### end Alembic commands ###