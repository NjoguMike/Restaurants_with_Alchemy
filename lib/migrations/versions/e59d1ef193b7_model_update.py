"""Model update

Revision ID: e59d1ef193b7
Revises: 1f21fb1a706f
Create Date: 2023-11-09 23:43:22.808687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e59d1ef193b7'
down_revision = '1f21fb1a706f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer_restaurant',
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('customer_id', 'restaurant_id')
    )
    op.drop_table('customer_reviews')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer_reviews',
    sa.Column('customer_id', sa.INTEGER(), nullable=False),
    sa.Column('review_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['review_id'], ['reviews.id'], ),
    sa.PrimaryKeyConstraint('customer_id', 'review_id')
    )
    op.drop_table('customer_restaurant')
    # ### end Alembic commands ###
