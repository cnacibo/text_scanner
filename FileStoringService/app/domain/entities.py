# app/domain/entities.py
from dataclasses import dataclass

@dataclass
class StoredFile:
    id: str
    filename: str
    content: bytes
