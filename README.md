# AI Book Reader

This repository contains the scaffolding for the AI Book Reader product. It includes:

- **frontend** – a Next.js 15 application that provides the user experience for browsing books, highlights, and AI insights.
- **backend** – a FastAPI service backed by SQLite for storing reader notes and bookmarks.

## Getting started

```bash
# Frontend
cd frontend
npm install
npm run dev

# Backend
cd ../backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The project also includes a `vercel.json` file configured to deploy both the frontend and backend to Vercel.
