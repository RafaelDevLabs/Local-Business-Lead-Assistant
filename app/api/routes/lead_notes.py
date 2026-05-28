from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.lead_note import LeadNote
from app.schemas.lead_note import LeadNoteCreate, LeadNoteRead
from app.services import lead_note_service

router = APIRouter()


@router.post("", response_model=LeadNoteRead, status_code=status.HTTP_201_CREATED)
def create_lead_note(
    lead_id: UUID,
    note_in: LeadNoteCreate,
    db: Session = Depends(get_db),
) -> LeadNote:
    try:
        return lead_note_service.create_note(db, lead_id, note_in)
    except lead_note_service.LeadNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lead not found",
        )


@router.get("", response_model=list[LeadNoteRead])
def list_lead_notes(
    lead_id: UUID,
    db: Session = Depends(get_db),
) -> list[LeadNote]:
    try:
        return lead_note_service.list_notes(db, lead_id)
    except lead_note_service.LeadNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lead not found",
        )
