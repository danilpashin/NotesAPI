from app.crud import notes_crud as notes_crud
from app.models.note_models import NoteCreate, NoteResponse


class NoteService:
    @staticmethod
    def get_all_notes() -> list[NoteResponse]:
        return notes_crud.get_all_notes()

    @staticmethod
    def get_note_by_id(note_id: int) -> NoteResponse | None:
        note = notes_crud.get_note_by_id(note_id)
        if not note:
            return None
        return note

    @staticmethod
    def create_note(note: NoteCreate) -> NoteResponse:
        if len(note.title) < 3:
            raise ValueError("Title too short")
        return notes_crud.create_note(note)