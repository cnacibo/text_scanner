# app/infrastructure/repositories.py
import uuid
from sqlalchemy.orm import Session
from app.domain.entities import TextStatistics
from app.domain.interfaces import AnalysisRepository
from app.domain.models import AnalysisResult

class SQLAnalysisRepository(AnalysisRepository):
    def __init__(self, db: Session):
        self.db = db

    def save(self, content: str, stats: TextStatistics) -> str:
        result = AnalysisResult(
            id=str(uuid.uuid4()),
            content=content,
            word_count=stats.word_count,
            char_count=stats.char_count,
            paragraph_count=stats.paragraph_count
        )
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)
        return result.id

    def get(self, analysis_id: str) -> TextStatistics:
        result = self.db.query(AnalysisResult).filter_by(id=analysis_id).first()
        if not result:
            raise ValueError("Not found")
        return TextStatistics(
            word_count=result.word_count,
            char_count=result.char_count,
            paragraph_count=result.paragraph_count
        )
