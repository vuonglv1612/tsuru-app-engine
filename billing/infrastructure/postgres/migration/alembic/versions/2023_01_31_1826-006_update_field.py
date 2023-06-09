"""Update field

Revision ID: 006
Revises: 005
Create Date: 2023-01-31 18:26:35.350329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '006'
down_revision = '005'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscription', sa.Column('current_period_amount', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('subscription', 'current_period_amount')
    # ### end Alembic commands ###
