"""Descripción del cambio

Revision ID: fd486a00a667
Revises: 
Create Date: 2025-02-28 16:33:23.690015

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd486a00a667'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('registro_acceso',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('plate', sa.String(length=50), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('tipo', sa.Enum('ENTRADA', 'SALIDA', name='tipoacceso'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('registro_acceso', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_registro_acceso_plate'), ['plate'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('registro_acceso', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_registro_acceso_plate'))

    op.drop_table('registro_acceso')
    # ### end Alembic commands ###
