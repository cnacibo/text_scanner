# app/domain/interfaces.py
from abc import ABC, abstractmethod
from .entities import TextStatistics

class FileContentProvider(ABC):
    @abstractmethod
    async def get_content(self, file_id: str) -> str:
        pass

class AnalysisRepository(ABC):
    @abstractmethod
    def save(self, content: str, stats: TextStatistics) -> str:
        pass

    @abstractmethod
    def get(self, analysis_id: str) -> TextStatistics:
        pass
