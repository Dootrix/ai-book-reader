# AI Book Reader Backend

This directory contains a FastAPI application that provides the API for storing notes and bookmarks captured while reading.

## Getting started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API uses a local SQLite database stored in `app.db`. Tables are created automatically on startup.
