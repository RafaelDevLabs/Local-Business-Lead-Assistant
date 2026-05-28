from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr

from app.core.enums import LeadStatus


class LeadCreate(BaseModel):
    name: str
    email: EmailStr | None = None
    phone: str
    service_interest: str | None = None
    preferred_date: datetime | None = None
    message: str | None = None


class LeadRead(BaseModel):
    id: UUID
    name: str
    email: EmailStr | None
    phone: str
    service_interest: str | None
    preferred_date: datetime | None
    message: str | None
    status: LeadStatus
    ai_summary: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class LeadUpdateStatus(BaseModel):
    status: LeadStatus


class LeadPage(BaseModel):
    items: list[LeadRead]
    total: int
    page: int
    limit: int
    pages: int
