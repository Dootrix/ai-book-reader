from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.models import note, schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.Note])
def get_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all notes with pagination"""
    notes = db.query(note.Note).offset(skip).limit(limit).all()
    return notes

@router.get("/{note_id}", response_model=schemas.Note)
def get_note(note_id: int, db: Session = Depends(get_db)):
    """Get a specific note by ID"""
    db_note = db.query(note.Note).filter(note.Note.id == note_id).first()
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@router.post("/", response_model=schemas.Note)
def create_note(note_data: schemas.NoteCreate, db: Session = Depends(get_db)):
    """Create a new note"""
    db_note = note.Note(**note_data.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@router.put("/{note_id}", response_model=schemas.Note)
def update_note(note_id: int, note_data: schemas.NoteUpdate, db: Session = Depends(get_db)):
    """Update an existing note"""
    db_note = db.query(note.Note).filter(note.Note.id == note_id).first()
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    
    update_data = note_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_note, field, value)
    
    db.commit()
    db.refresh(db_note)
    return db_note

@router.delete("/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    """Delete a note"""
    db_note = db.query(note.Note).filter(note.Note.id == note_id).first()
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    
    db.delete(db_note)
    db.commit()
    return {"message": "Note deleted successfully"}