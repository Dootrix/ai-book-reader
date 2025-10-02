"""FastAPI application entry point for the AI Book Reader backend."""
from __future__ import annotations

from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

# Import models for side effects so SQLAlchemy is aware of them when metadata is created.
from . import crud, models, schemas  # noqa: F401
from .database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Book Reader API",
    version="0.1.0",
    description=(
        "Backend service that stores notes and bookmarks captured while reading books. "
        "The service exposes simple CRUD style endpoints that can be expanded as the "
        "product matures."
    ),
)


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    """Return a basic readiness indicator."""
    return {"status": "ok"}


@app.get("/notes", response_model=List[schemas.NoteRead], tags=["notes"])
def get_notes(db: Session = Depends(get_db)):
    """List all notes stored in the database."""
    return crud.list_notes(db)


@app.post("/notes", response_model=schemas.NoteRead, status_code=201, tags=["notes"])
def post_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    """Create a new note for a reader."""
    return crud.create_note(db, note)


@app.get("/bookmarks", response_model=List[schemas.BookmarkRead], tags=["bookmarks"])
def get_bookmarks(db: Session = Depends(get_db)):
    """List all bookmarks stored in the database."""
    return crud.list_bookmarks(db)


@app.post(
    "/bookmarks",
    response_model=schemas.BookmarkRead,
    status_code=201,
    tags=["bookmarks"],
)
def post_bookmark(bookmark: schemas.BookmarkCreate, db: Session = Depends(get_db)):
    """Create a new bookmark for a reader."""
    return crud.create_bookmark(db, bookmark)
