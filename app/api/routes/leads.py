from typing import Literal
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status as http_status
from sqlalchemy.orm import Session

from app.core.enums import LeadStatus
from app.db.session import get_db
from app.models.lead import Lead
from app.schemas.lead import LeadCreate, LeadPage, LeadRead, LeadUpdateStatus
from app.services import lead_service

router = APIRouter()


@router.post("", response_model=LeadRead, status_code=http_status.HTTP_201_CREATED)
def create_lead(lead_in: LeadCreate, db: Session = Depends(get_db)) -> Lead:
    return lead_service.create_lead(db, lead_in)


@router.get("", response_model=LeadPage)
def list_leads(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100),
    status: LeadStatus | None = None,
    search: str | None = Query(default=None, min_length=1),
    sort_order: Literal["asc", "desc"] = Query(default="desc"),
    db: Session = Depends(get_db),
) -> LeadPage:
    items, total, pages = lead_service.list_leads(
        db,
        page=page,
        limit=limit,
        status=status,
        search=search,
        sort_order=sort_order,
    )
    return LeadPage(items=items, total=total, page=page, limit=limit, pages=pages)


@router.get("/{lead_id}", response_model=LeadRead)
def get_lead(lead_id: UUID, db: Session = Depends(get_db)) -> Lead:
    lead = lead_service.get_lead(db, lead_id)
    if lead is None:
        raise HTTPException(
            status_code=http_status.HTTP_404_NOT_FOUND,
            detail="Lead not found",
        )
    return lead


@router.patch("/{lead_id}/status", response_model=LeadRead)
def update_lead_status(
    lead_id: UUID,
    status_in: LeadUpdateStatus,
    db: Session = Depends(get_db),
) -> Lead:
    lead = lead_service.get_lead(db, lead_id)
    if lead is None:
        raise HTTPException(
            status_code=http_status.HTTP_404_NOT_FOUND,
            detail="Lead not found",
        )

    return lead_service.update_lead_status(db, lead, status_in.status)
