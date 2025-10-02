"""ORM models used by the AI Book Reader backend."""
from __future__ import annotations

from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from .database import Base


class Note(Base):
    """A note that a reader has taken for a specific book."""

    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(255), nullable=False, index=True)
    book_title = Column(String(512), nullable=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class Bookmark(Base):
    """A bookmark that stores the reader's location in a book."""

    __tablename__ = "bookmarks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(255), nullable=False, index=True)
    book_title = Column(String(512), nullable=False)
    location = Column(String(255), nullable=False)
    note = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
