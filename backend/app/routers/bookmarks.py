from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models
from ..database import get_db
from ..schemas.bookmark import BookmarkCreate, BookmarkRead

router = APIRouter(prefix="/bookmarks", tags=["bookmarks"])


@router.post("", response_model=BookmarkRead, status_code=status.HTTP_201_CREATED)
def create_bookmark(payload: BookmarkCreate, db: Session = Depends(get_db)) -> BookmarkRead:
    bookmark = models.Bookmark(**payload.model_dump())
    db.add(bookmark)
    db.commit()
    db.refresh(bookmark)
    return BookmarkRead.model_validate(bookmark)


@router.get("", response_model=list[BookmarkRead])
def list_bookmarks(db: Session = Depends(get_db)) -> list[BookmarkRead]:
    bookmarks = db.query(models.Bookmark).order_by(models.Bookmark.id.desc()).all()
    return [BookmarkRead.model_validate(bookmark) for bookmark in bookmarks]


@router.get("/{bookmark_id}", response_model=BookmarkRead)
def get_bookmark(bookmark_id: int, db: Session = Depends(get_db)) -> BookmarkRead:
    bookmark = db.query(models.Bookmark).filter(models.Bookmark.id == bookmark_id).first()
    if bookmark is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bookmark not found")
    return BookmarkRead.model_validate(bookmark)
