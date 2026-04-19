from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette import status

from app.database.database import get_db
from app.models.note_models import NoteResponse, NoteCreate, NoteUpdate
from app.crud.notes_crud import NoteRepository
from app.services.notes_service import NoteService

router = APIRouter()

def get_note_service(db: Session = Depends(get_db)) -> NoteService:
    crud = NoteRepository(db)
    return NoteService(crud)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=NoteResponse)
def create_note(note: NoteCreate, service: NoteService = Depends(get_note_service)):
    try:
        return service.create_note(note)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/{note_id}", response_model=NoteResponse)
def get_note(note_id: int, service: NoteService = Depends(get_note_service)):
    note = service.get_note_by_id(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.get("/", response_model=list[NoteResponse])
def list_notes(service: NoteService = Depends(get_note_service)):
    return service.get_all_notes()

@router.put("/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, note_update: NoteUpdate, service: NoteService = Depends(get_note_service)):
    old_note = service.get_note_by_id(note_id)
    if not old_note:
        raise HTTPException(status_code=404, detail="Note not found")
    try:
        return service.update_note_service(note_id, note_update)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, service: NoteService = Depends(get_note_service)):
    deleted = service.delete_note_service(note_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Note with id {note_id} not found")