from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.models import bookmark, schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.Bookmark])
def get_bookmarks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all bookmarks with pagination"""
    bookmarks = db.query(bookmark.Bookmark).offset(skip).limit(limit).all()
    return bookmarks

@router.get("/{bookmark_id}", response_model=schemas.Bookmark)
def get_bookmark(bookmark_id: int, db: Session = Depends(get_db)):
    """Get a specific bookmark by ID"""
    db_bookmark = db.query(bookmark.Bookmark).filter(bookmark.Bookmark.id == bookmark_id).first()
    if db_bookmark is None:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return db_bookmark

@router.post("/", response_model=schemas.Bookmark)
def create_bookmark(bookmark_data: schemas.BookmarkCreate, db: Session = Depends(get_db)):
    """Create a new bookmark"""
    db_bookmark = bookmark.Bookmark(**bookmark_data.dict())
    db.add(db_bookmark)
    db.commit()
    db.refresh(db_bookmark)
    return db_bookmark

@router.put("/{bookmark_id}", response_model=schemas.Bookmark)
def update_bookmark(bookmark_id: int, bookmark_data: schemas.BookmarkUpdate, db: Session = Depends(get_db)):
    """Update an existing bookmark"""
    db_bookmark = db.query(bookmark.Bookmark).filter(bookmark.Bookmark.id == bookmark_id).first()
    if db_bookmark is None:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    
    update_data = bookmark_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_bookmark, field, value)
    
    db.commit()
    db.refresh(db_bookmark)
    return db_bookmark

@router.delete("/{bookmark_id}")
def delete_bookmark(bookmark_id: int, db: Session = Depends(get_db)):
    """Delete a bookmark"""
    db_bookmark = db.query(bookmark.Bookmark).filter(bookmark.Bookmark.id == bookmark_id).first()
    if db_bookmark is None:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    
    db.delete(db_bookmark)
    db.commit()
    return {"message": "Bookmark deleted successfully"}