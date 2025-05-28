from app.domain.interfaces import FileStorage
from app.domain.models import File as  FileMetadata
from app.infrastructure.repositories import FileRepository
from sqlalchemy.orm import Session

class SaveFileUseCase:
    def __init__(self, storage: FileStorage, repo, db):
        self.storage = storage
        self.repo = repo
        self.db = db

    def execute(self, filename: str, content: bytes) -> str:
        file_id, location = self.storage.save(filename, content)
        self.repo.save(file_id, filename, location)
        return file_id
