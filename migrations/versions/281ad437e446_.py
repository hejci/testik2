"""empty message

Revision ID: 281ad437e446
Revises: fc247e501ee7
Create Date: 2023-10-02 11:10:52.011444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '281ad437e446'
down_revision = 'fc247e501ee7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('typ_vozidla',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vyrobce_vozidla', sa.String(length=50), nullable=True),
    sa.Column('vyrobce_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['vyrobce_id'], ['vyrobce.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('typ_vozidla')
    # ### end Alembic commands ###
