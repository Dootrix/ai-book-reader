# AI Book Reader

AI assisted book reader project scaffold.

## Structure

- `frontend/` – Next.js 15 + React TypeScript frontend scaffold with a landing page and linting.
- `backend/` – FastAPI backend configured with SQLite persistence for notes and bookmarks.

## Getting started

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

SQLite data is stored in `backend/app.db` by default. Adjust `database_url` in
`backend/app/core/config.py` if you need a different location.
