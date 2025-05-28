# app/use_cases/analyze_text.py
from app.domain.entities import TextStatistics
from app.domain.interfaces import FileContentProvider, AnalysisRepository

class AnalyzeTextUseCase:
    def __init__(self, content_provider: FileContentProvider, repository: AnalysisRepository):
        self.content_provider = content_provider
        self.repository = repository

    async def execute(self, file_id: str) -> str:
        content = await self.content_provider.get_content(file_id)
        if not content:
            raise ValueError("Content is empty")

        paragraphs = [p for p in content.split('\n') if p.strip()]
        words = content.split()
        stats = TextStatistics(
            word_count=len(words),
            char_count=len(content),
            paragraph_count=len(paragraphs)
        )

        analysis_id = self.repository.save(content, stats)
        return analysis_id
