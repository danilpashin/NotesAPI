from datetime import datetime
from app.models.note_models import NoteResponse, NoteCreate

_mock_notes = []
_counter = 1

def get_all_notes():
    return _mock_notes

def get_note_by_id(note_id: int):
    return {
        "id": note_id,
        "title": "Пример заметки",
        "content": "Содержание",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": None
    }

def create_note(note: NoteCreate):
    global _counter
    new_note = NoteResponse(
        id=_counter,
        title=note.title,
        content=note.content,
        createdAt="2026-01-01T00:00:00"
    )
    _counter += 1
    _mock_notes.append(new_note)
    return new_note