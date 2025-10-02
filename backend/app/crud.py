"""CRUD helpers for the AI Book Reader backend."""
from __future__ import annotations

from typing import Iterable

from sqlalchemy.orm import Session

from . import models, schemas


def list_notes(db: Session) -> Iterable[models.Note]:
    return db.query(models.Note).order_by(models.Note.created_at.desc()).all()


def create_note(db: Session, note_in: schemas.NoteCreate) -> models.Note:
    note = models.Note(**note_in.model_dump())
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


def list_bookmarks(db: Session) -> Iterable[models.Bookmark]:
    return db.query(models.Bookmark).order_by(models.Bookmark.created_at.desc()).all()


def create_bookmark(db: Session, bookmark_in: schemas.BookmarkCreate) -> models.Bookmark:
    bookmark = models.Bookmark(**bookmark_in.model_dump())
    db.add(bookmark)
    db.commit()
    db.refresh(bookmark)
    return bookmark
