"""Pydantic schemas for request and response bodies."""
from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class NoteBase(BaseModel):
    user_id: str = Field(..., description="Identifier of the reader the note belongs to")
    book_title: Optional[str] = Field(None, description="Title of the book the note references")
    content: str = Field(..., description="Free-form note content")


class NoteCreate(NoteBase):
    pass


class NoteRead(NoteBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class BookmarkBase(BaseModel):
    user_id: str = Field(..., description="Identifier of the reader")
    book_title: str = Field(..., description="Title of the referenced book")
    location: str = Field(..., description="A string describing where the reader stopped")
    note: Optional[str] = Field(None, description="Optional annotation for the bookmark")


class BookmarkCreate(BookmarkBase):
    pass


class BookmarkRead(BookmarkBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
