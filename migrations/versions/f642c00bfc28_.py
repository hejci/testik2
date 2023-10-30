"""empty message

Revision ID: f642c00bfc28
Revises: 54c42a7c991c
Create Date: 2023-10-02 10:46:27.660993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f642c00bfc28'
down_revision = '54c42a7c991c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vyrobce', schema=None) as batch_op:
        batch_op.add_column(sa.Column('identifikator', sa.Integer(), nullable=True))
        batch_op.create_unique_constraint(None, ['identifikator'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vyrobce', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('identifikator')

    # ### end Alembic commands ###