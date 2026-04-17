from app.models.note_models import NoteCreate, NoteResponse
from app.crud.notes_crud import NoteCrud


class NoteService:
    def __init__(self, crud: NoteCrud):
        self.crud = crud

    def get_all_notes(self) -> list[NoteResponse]:
        return self.crud.get_all_notes()

    def get_note_by_id(self, note_id: int) -> NoteResponse | None:
        note = self.crud.get_note_by_id(note_id)
        if not note:
            return None
        return note

    def create_note(self, note: NoteCreate) -> NoteResponse:
        if len(note.title) < 3:
            raise ValueError("Title too short")
        return self.crud.create_note(note)