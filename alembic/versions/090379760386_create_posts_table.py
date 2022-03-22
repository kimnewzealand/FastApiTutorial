"""Create posts table

Revision ID: 090379760386
Revises: 
Create Date: 2022-03-22 09:34:22.972246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '090379760386'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # op.create_table('posts', sa.Column(
    #    'id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    op.add_column(sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
