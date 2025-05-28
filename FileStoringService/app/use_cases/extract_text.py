# app/use_cases/extract_text.py
from app.domain.interfaces import FileStorage, TextExtractor

class ExtractTextUseCase:
    def __init__(self, storage: FileStorage, extractor: TextExtractor, repo, db):
        self.storage = storage
        self.extractor = extractor
        self.repo = repo
        self.db = db

    def execute(self, file_id: str) -> str:
        location = self.repo.get_location(file_id)
        file = self.storage.get_by_location(location)
        return self.extractor.extract_text(file)

