# Backend Scaffold

FastAPI backend exposing endpoints for managing notes and bookmarks stored in a SQLite database.

## Getting started

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API will be available at [http://localhost:8000](http://localhost:8000). Interactive docs are
served from `/docs` and `/redoc` once the server is running.
