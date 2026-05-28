"""add lead indexes

Revision ID: 20260528_0002
Revises: 20260528_0001
Create Date: 2026-05-28 00:00:00.000000
"""
from collections.abc import Sequence

from alembic import op

revision: str = "20260528_0002"
down_revision: str | None = "20260528_0001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_index("ix_leads_status", "leads", ["status"])
    op.create_index("ix_leads_created_at", "leads", ["created_at"])
    op.create_index("ix_leads_phone", "leads", ["phone"])


def downgrade() -> None:
    op.drop_index("ix_leads_phone", table_name="leads")
    op.drop_index("ix_leads_created_at", table_name="leads")
    op.drop_index("ix_leads_status", table_name="leads")
