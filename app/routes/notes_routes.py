from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.note_models import NoteResponse, NoteCreate
from app.crud.notes_crud import NoteCrud
from app.services.notes_service import NoteService

router = APIRouter()

def get_note_service(db: Session = Depends(get_db)) -> NoteService:
    crud = NoteCrud(db)
    return NoteService(crud)

@router.post("/", response_model=NoteResponse)
def create_note(note: NoteCreate, service: NoteService = Depends(get_note_service)):
    return service.create_note(note)

@router.get("/{note_id}", response_model=NoteResponse)
def get_note(note_id: int, service: NoteService = Depends(get_note_service)):
    note = service.get_note_by_id(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.get("/", response_model=list[NoteResponse])
def list_notes(service: NoteService = Depends(get_note_service)):
    return service.get_all_notes()