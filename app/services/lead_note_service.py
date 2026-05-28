from uuid import UUID

from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from app.models.lead import Lead
from app.models.lead_note import LeadNote
from app.schemas.lead_note import LeadNoteCreate


class LeadNotFoundError(Exception):
    pass


def create_note(db: Session, lead_id: UUID, note_in: LeadNoteCreate) -> LeadNote:
    if db.get(Lead, lead_id) is None:
        raise LeadNotFoundError

    note = LeadNote(lead_id=lead_id, note=note_in.note)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


def list_notes(db: Session, lead_id: UUID) -> list[LeadNote]:
    if db.get(Lead, lead_id) is None:
        raise LeadNotFoundError

    return list(
        db.scalars(
            select(LeadNote)
            .where(LeadNote.lead_id == lead_id)
            .order_by(desc(LeadNote.created_at))
        ).all()
    )
