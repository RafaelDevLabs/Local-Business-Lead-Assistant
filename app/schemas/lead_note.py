from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class LeadNoteCreate(BaseModel):
    note: str = Field(min_length=1)


class LeadNoteRead(BaseModel):
    id: UUID
    lead_id: UUID
    note: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
