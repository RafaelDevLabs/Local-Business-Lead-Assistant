from fastapi import APIRouter

from app.api.routes import health, lead_notes, leads

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(leads.router, prefix="/api/leads", tags=["leads"])
api_router.include_router(
    lead_notes.router,
    prefix="/api/leads/{lead_id}/notes",
    tags=["lead notes"],
)
