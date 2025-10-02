from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Note schemas
class NoteBase(BaseModel):
    title: str
    content: str
    book_title: str
    page_number: Optional[int] = None
    chapter: Optional[str] = None

class NoteCreate(NoteBase):
    pass

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    book_title: Optional[str] = None
    page_number: Optional[int] = None
    chapter: Optional[str] = None

class Note(NoteBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Bookmark schemas
class BookmarkBase(BaseModel):
    book_title: str
    page_number: int
    chapter: Optional[str] = None
    quote: Optional[str] = None
    notes: Optional[str] = None
    is_favorite: bool = False

class BookmarkCreate(BookmarkBase):
    pass

class Bookmark(BookmarkBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True