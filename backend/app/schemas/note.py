from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class NoteBase(BaseModel):
    title: str = Field(..., max_length=255)
    content: str
    page: int | None = Field(default=None, ge=0)


class NoteCreate(NoteBase):
    pass


class NoteRead(NoteBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
