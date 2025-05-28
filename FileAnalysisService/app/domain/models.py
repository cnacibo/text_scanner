# FileAnalysisService/app/db/models.py
from sqlalchemy import Column, String, UUID, ForeignKey, Integer
from ..infrastructure.database import Base

class AnalysisResult(Base):
    __tablename__ = 'analysis'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    content = Column(String)
    word_count = Column(Integer)
    char_count = Column(Integer)
    paragraph_count = Column(Integer)