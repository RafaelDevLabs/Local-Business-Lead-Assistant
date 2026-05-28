import json
import logging
from html import escape
from re import sub
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from app.core.config import Settings, get_settings
from app.models.lead import Lead

logger = logging.getLogger(__name__)

RESEND_EMAILS_URL = "https://api.resend.com/emails"


def send_new_lead_notification(
    lead: Lead,
    settings: Settings | None = None,
) -> bool:
    settings = settings or get_settings()

    if (
        not settings.resend_api_key
        or not settings.business_notification_email
        or not settings.email_from
    ):
        logger.warning(
            "Skipping lead notification email because RESEND_API_KEY, "
            "BUSINESS_NOTIFICATION_EMAIL, or EMAIL_FROM is missing"
        )
        return False

    payload = {
        "from": settings.email_from,
        "to": [settings.business_notification_email],
        "subject": "New Lead Received",
        "html": _build_email_html(lead),
    }
    request = Request(
        RESEND_EMAILS_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {settings.resend_api_key}",
            "Content-Type": "application/json",
            "User-Agent": "local-business-lead-assistant/1.0",
        },
        method="POST",
    )

    try:
        with urlopen(request, timeout=15) as response:
            return 200 <= response.status < 300
    except HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        logger.exception("Failed to send lead notification email: %s", error_body)
    except URLError:
        logger.exception("Failed to send lead notification email")

    return False


def _build_email_body(lead: Lead) -> str:
    return _build_email_html(lead)


def _build_email_html(lead: Lead) -> str:
    whatsapp_url = _build_whatsapp_url(lead.phone)
    whatsapp_section = (
        f'<p><a href="{whatsapp_url}">Open WhatsApp chat</a></p>'
        if whatsapp_url
        else "<p>Phone number not available.</p>"
    )

    return f"""
<h2>New Lead Received</h2>

<h3>Lead Details</h3>
<p><strong>Name:</strong> {escape(lead.name)}</p>
<p><strong>Phone:</strong> {escape(lead.phone or "Not provided")}</p>
<p><strong>Email:</strong> {escape(lead.email or "Not provided")}</p>
<p><strong>Service interest:</strong> {escape(lead.service_interest or "Not provided")}</p>
<p><strong>Preferred date:</strong> {escape(str(lead.preferred_date or "Not provided"))}</p>
<p><strong>Message:</strong><br>{escape(lead.message or "Not provided")}</p>

<h3>AI Summary</h3>
<p>{escape(lead.ai_summary or "Not available").replace(chr(10), "<br>")}</p>

<h3>WhatsApp Contact</h3>
{whatsapp_section}
""".strip()


def _build_whatsapp_url(phone: str | None) -> str | None:
    if not phone:
        return None

    digits = sub(r"\D", "", phone)
    return f"https://wa.me/{digits}" if digits else None
