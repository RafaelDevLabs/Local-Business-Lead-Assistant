# Local Business Lead Assistant

MVP for a local business lead capture and follow-up assistant.

The project currently includes:

- FastAPI backend with PostgreSQL persistence
- SQLAlchemy 2.x models and Alembic migrations
- Lead CRUD with pagination, filtering, search, and sorting
- Lead status updates
- Lead notes for simple CRM follow-up
- Local AI lead summaries through LM Studio's OpenAI-compatible API
- Resend email notifications for new leads
- Next.js public landing page
- Public lead form connected to the backend

## Project Structure

```text
.
+-- app/                 # FastAPI backend
+-- alembic/             # Database migrations
+-- frontend/            # Next.js frontend
+-- requirements.txt     # Backend Python dependencies
+-- alembic.ini
+-- .env.example         # Backend environment template
+-- README.md
```

## Backend Stack

- Python 3.11+
- FastAPI
- SQLAlchemy 2.x
- Pydantic v2
- PostgreSQL
- Alembic
- pydantic-settings
- OpenAI Python client configured for LM Studio
- Resend email API

## Frontend Stack

- Next.js
- TypeScript
- Tailwind CSS
- App Router
- Plain React state for the lead form

## Backend Setup

From the project root:

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
copy .env.example .env
```

Edit `.env` with your local values.

Required for database:

```env
DATABASE_URL=postgresql+psycopg://postgres:your_password@localhost:5432/local_business_leads
```

Optional local AI settings:

```env
LLM_BASE_URL=http://127.0.0.1:1234/v1
LLM_MODEL=qwen/qwen3-coder-30b
LLM_API_KEY=not-needed
```

Optional email settings:

```env
BUSINESS_NOTIFICATION_EMAIL=you@example.com
EMAIL_FROM="Local Business Lead Assistant <onboarding@resend.dev>"
RESEND_API_KEY=your_resend_api_key
```

Do not commit `.env`.

## Database

Create the PostgreSQL database:

```cmd
"C:\Program Files\PostgreSQL\18\bin\createdb.exe" -U postgres local_business_leads
```

Apply migrations:

```cmd
alembic upgrade head
```

Current migrations include:

- leads table
- useful indexes for leads
- lead_notes table

## Run Backend

```cmd
.venv\Scripts\activate.bat
uvicorn app.main:app --reload
```

Backend URLs:

```text
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs
```

## Backend API

Health:

```text
GET /health
```

Leads:

```text
POST  /api/leads
GET   /api/leads
GET   /api/leads/{lead_id}
PATCH /api/leads/{lead_id}/status
```

Lead list query params:

```text
page
limit
status
search
sort_order
```

Lead notes:

```text
POST /api/leads/{lead_id}/notes
GET  /api/leads/{lead_id}/notes
```

## AI Summary Behavior

When a lead is created:

1. The lead is saved first.
2. The backend tries to generate a short lead summary through LM Studio.
3. The summary is saved into `ai_summary` if generation succeeds.
4. The backend sends an email notification if email settings are configured.

If AI or email fails, the lead remains saved and the request does not crash.

The prompt asks for exactly four practical bullet points:

```text
- Intent:
- Urgency:
- Key Need:
- Recommended Follow-up:
```

The backend also strips unexpected Chinese, Japanese, and Korean characters from the final summary before saving.

## Frontend Setup

From the frontend folder:

```cmd
cd frontend
npm install
copy .env.example .env.local
```

`frontend/.env.local` should contain:

```env
NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000
```

## Run Frontend

```cmd
cd frontend
npm run dev
```

Frontend URL:

```text
http://localhost:3000
```

The current frontend includes:

- public landing page for "Local Growth Studio"
- value proposition section
- services section
- public lead/contact form
- client-side validation for name and phone
- loading, success, and error states

## Typical Local Development

Terminal 1:

```cmd
.venv\Scripts\activate.bat
uvicorn app.main:app --reload
```

Terminal 2:

```cmd
cd frontend
npm run dev
```

Then open:

```text
http://localhost:3000
```

## What Is Not Included Yet

- Admin dashboard
- Authentication
- User accounts
- Deployment setup
- Background workers
- Redis
- Celery
- Complex state management
- React Query
- Form libraries

## Git Notes

Ignored files include:

- `.env`
- `.venv/`
- `frontend/node_modules/`
- `frontend/.next/`
- local logs and OS files
