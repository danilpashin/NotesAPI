from app.models.note_models import NoteCreate, NoteResponse, NoteUpdate
from app.crud.notes_crud import NoteRepository


class NoteService:
    def __init__(self, crud: NoteRepository):
        self.crud = crud

    def get_all_notes(self) -> list[NoteResponse]:
        notes = self.crud.get_all_notes()
        return notes

    def get_note_by_id(self, note_id: int) -> NoteResponse | None:
        note = self.crud.get_note_by_id(note_id)
        if not note:
            return None
        return note

    def create_note(self, note: NoteCreate) -> NoteResponse:
        if len(note.title) < 3:
            raise ValueError("Title too short")
        return self.crud.create_note(note)

    def update_note_service(self, note_id: int, note: NoteUpdate) -> NoteResponse:
        if len(note.title) < 3:
            raise ValueError("Title too short")
        return self.crud.update_note(note_id, note)

    def delete_note_service(self, note_id: int) -> bool:
        return self.crud.delete_note(note_id)