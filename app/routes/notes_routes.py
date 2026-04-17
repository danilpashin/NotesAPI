from fastapi import APIRouter, HTTPException
from app.models.note_models import NoteResponse, NoteCreate
import app.crud.notes_crud as note_crud

router = APIRouter()

@router.post("/", response_model=NoteResponse)
def create_note_endpoint(note: NoteCreate):
    return note_crud.create_note(note)

@router.get("/{note_id}", response_model=NoteResponse)
def get_note(note_id: int):
    note = note_crud.get_note_by_id(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.get("/", response_model=list[NoteResponse])
def list_notes():
    return note_crud.get_all_notes()