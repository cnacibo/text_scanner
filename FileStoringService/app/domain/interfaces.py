# app/domain/interfaces.py
from abc import ABC, abstractmethod
from .entities import StoredFile

class FileStorage(ABC):
    @abstractmethod
    def save(self, filename: str, content: bytes) -> str:
        pass

    @abstractmethod
    def get_by_location(self, location: str):
        pass

class TextExtractor(ABC):
    @abstractmethod
    def extract_text(self, file: StoredFile) -> str:
        pass
