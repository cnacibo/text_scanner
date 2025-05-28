# app/infrastructure/local_storage.py
import os
import uuid
from app.domain.entities import StoredFile
from app.domain.interfaces import FileStorage
from pathlib import Path

STORAGE_DIR = Path("/app/storage")
STORAGE_DIR.mkdir(parents=True, exist_ok=True)

class LocalFileStorage(FileStorage):
    def save(self, filename: str, content: bytes) -> tuple[str, str]:
        file_id = str(uuid.uuid4())
        path = STORAGE_DIR / file_id
        with open(path, "wb") as f:
            f.write(content)
        return file_id, str(path)


    def get_by_location(self, location: str) -> StoredFile:
        if not os.path.exists(location):
            raise FileNotFoundError("File not found at given location")
        with open(location, "rb") as f:
            content = f.read()
        return StoredFile(id=None, filename=os.path.basename(location), content=content)

