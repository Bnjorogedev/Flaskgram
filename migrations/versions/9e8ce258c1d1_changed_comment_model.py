"""changed comment model

Revision ID: 9e8ce258c1d1
Revises: ddc1473ca2bf
Create Date: 2020-08-30 19:25:27.156751

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9e8ce258c1d1'
down_revision = 'ddc1473ca2bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('author', sa.String(length=100), nullable=True))
    op.drop_constraint('fk_comment_post_id_user', 'comment', type_='foreignkey')
    op.create_foreign_key(None, 'comment', 'user', ['author'], ['id'])
    op.create_foreign_key(None, 'comment', 'post', ['post_id'], ['id'])
    op.drop_column('comment', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('title', mysql.VARCHAR(length=100), nullable=False))
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.create_foreign_key('fk_comment_post_id_user', 'comment', 'user', ['post_id'], ['id'])
    op.drop_column('comment', 'author')
    # ### end Alembic commands ###
