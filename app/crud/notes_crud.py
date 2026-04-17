from datetime import datetime
from app.database import NoteDB
from app.models.note_models import NoteCreate, NoteUpdate
from sqlalchemy.orm import Session


class NoteRepository:
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

    def update_note(self, note_id: int, note: NoteUpdate) -> NoteDB | None:
        db_note = self.db.query(NoteDB).filter(NoteDB.id == note_id).first()
        if not db_note:
            return None

        update_dict = note.model_dump(exclude_unset=True)
        for key, value in update_dict.items():
            setattr(db_note, key, value)

        self.db.commit()
        self.db.refresh(db_note)
        return db_note

    def delete_note(self, note_id: int) -> bool:
        note = self.db.query(NoteDB).filter(NoteDB.id == note_id).first()
        if not note:
            return False
        self.db.delete(note)
        self.db.commit()
        return True