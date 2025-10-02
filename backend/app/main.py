from fastapi import FastAPI

from . import models
from .database import Base, engine
from .routers import bookmarks, notes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Book Reader API")

app.include_router(notes.router)
app.include_router(bookmarks.router)


@app.get("/health", tags=["health"])  # pragma: no cover - trivial endpoint
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
