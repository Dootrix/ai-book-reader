from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from ..database import Base


class Bookmark(Base):
    __tablename__ = "bookmarks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    book_title: Mapped[str] = mapped_column(String(255), nullable=False)
    page: Mapped[int] = mapped_column(Integer, nullable=False)
    note: Mapped[str | None] = mapped_column(String, nullable=True)
