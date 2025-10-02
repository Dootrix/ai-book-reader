from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models
from ..database import get_db
from ..schemas.note import NoteCreate, NoteRead

router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("", response_model=NoteRead, status_code=status.HTTP_201_CREATED)
def create_note(payload: NoteCreate, db: Session = Depends(get_db)) -> NoteRead:
    note = models.Note(**payload.model_dump())
    db.add(note)
    db.commit()
    db.refresh(note)
    return NoteRead.model_validate(note)


@router.get("", response_model=list[NoteRead])
def list_notes(db: Session = Depends(get_db)) -> list[NoteRead]:
    notes = db.query(models.Note).order_by(models.Note.created_at.desc()).all()
    return [NoteRead.model_validate(note) for note in notes]


@router.get("/{note_id}", response_model=NoteRead)
def get_note(note_id: int, db: Session = Depends(get_db)) -> NoteRead:
    note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return NoteRead.model_validate(note)
