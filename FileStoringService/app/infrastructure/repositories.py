# app/infrastructure/repositories.py
from sqlalchemy.orm import Session
from app.domain.models import File as FileModel

class FileRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, file_id: str) -> FileModel | None:
        return self.db.query(FileModel).filter(FileModel.id == file_id).first()

    def save(self, file_id: str, filename: str, location: str):
        record = FileModel(id=file_id, filename=filename, location=location)
        self.db.add(record)
        self.db.commit()

    def get_location(self, file_id: str) -> str:
        record = self.db.query(FileModel).filter_by(id=file_id).first()
        if not record:
            raise FileNotFoundError("File metadata not found in DB")
        return record.location
