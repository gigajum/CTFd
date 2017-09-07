"""dynamic points

Revision ID: 772586ce9061
Revises: 1ec4a28fe0ff
Create Date: 2017-08-17 23:37:37.665813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '772586ce9061'
down_revision = '1ec4a28fe0ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('challenges', sa.Column('dynamic', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('challenges', 'dynamic')
    # ### end Alembic commands ###
