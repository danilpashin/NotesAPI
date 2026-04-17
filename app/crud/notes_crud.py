from datetime import datetime
from app.database import NoteDB
from app.models.note_models import NoteResponse, NoteCreate
from sqlalchemy.orm import Session


class NoteCrud:
    def __init__(self, db: Session):
        self.db = db

    def get_all_notes(self) -> list[NoteDB]:
        return self.db.query(NoteDB).all()

    def get_note_by_id(self, note_id: int) -> NoteDB | None:
        return self.db.query(NoteDB).filter(NoteDB.id == note_id).first()

    def create_note(self, note: NoteCreate) -> NoteDB:
        db_note = NoteDB(title=note.title, content=note.content)
        self.db.add(db_note)
        self.db.commit()
        self.db.refresh(db_note)
        return db_note