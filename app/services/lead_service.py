import math
from uuid import UUID

from sqlalchemy import asc, desc, func, or_, select
from sqlalchemy.orm import Session

from app.core.enums import LeadStatus
from app.models.lead import Lead
from app.schemas.lead import LeadCreate
from app.services import ai_summary_service, email_service


def create_lead(db: Session, lead_in: LeadCreate) -> Lead:
    lead = Lead(**lead_in.model_dump())
    db.add(lead)
    db.commit()
    db.refresh(lead)

    summary = ai_summary_service.generate_lead_summary(lead)
    if summary:
        lead.ai_summary = summary
        db.commit()
        db.refresh(lead)

    email_service.send_new_lead_notification(lead)
    return lead


def list_leads(
    db: Session,
    *,
    page: int,
    limit: int,
    status: LeadStatus | None = None,
    search: str | None = None,
    sort_order: str = "desc",
) -> tuple[list[Lead], int, int]:
    filters = []

    if status is not None:
        filters.append(Lead.status == status)

    clean_search = search.strip() if search else None
    if clean_search:
        search_value = f"%{clean_search}%"
        filters.append(
            or_(
                Lead.name.ilike(search_value),
                Lead.phone.ilike(search_value),
            )
        )

    order_by = asc(Lead.created_at) if sort_order == "asc" else desc(Lead.created_at)
    offset = (page - 1) * limit

    total_stmt = select(func.count()).select_from(Lead)
    query_stmt = select(Lead).order_by(order_by).offset(offset).limit(limit)

    if filters:
        total_stmt = total_stmt.where(*filters)
        query_stmt = query_stmt.where(*filters)

    total = db.scalar(total_stmt) or 0
    items = list(db.scalars(query_stmt).all())
    pages = math.ceil(total / limit) if total else 0

    return items, total, pages


def get_lead(db: Session, lead_id: UUID) -> Lead | None:
    return db.get(Lead, lead_id)


def update_lead_status(db: Session, lead: Lead, status: LeadStatus) -> Lead:
    lead.status = status
    db.commit()
    db.refresh(lead)
    return lead
