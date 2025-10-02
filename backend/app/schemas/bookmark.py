from pydantic import BaseModel, ConfigDict, Field


class BookmarkBase(BaseModel):
    book_title: str = Field(..., max_length=255)
    page: int = Field(..., ge=0)
    note: str | None = None


class BookmarkCreate(BookmarkBase):
    pass


class BookmarkRead(BookmarkBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
