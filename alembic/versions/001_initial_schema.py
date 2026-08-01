from typing import Sequence, Union

from alembic import op  #Operatins
import sqlalchemy as sa

revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # to store the prediction history in postgres
    op.create_table("prediction_history",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("store", sa.Integer(), nullable=True),
        sa.Column("item", sa.Integer(), nullable=True),
        sa.Column("prediction", sa.Float(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),)

    op.create_index(op.f("ix_prediction_history_id"),
        "prediction_history",
        ["id"],
        unique=False,)





    # to store the user info in postgres
    op.create_table("users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("password_hash", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),)

    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_users_id"), table_name="users")
    op.drop_table("users")
    op.drop_index(op.f("ix_prediction_history_id"), table_name="prediction_history")
    op.drop_table("prediction_history")
