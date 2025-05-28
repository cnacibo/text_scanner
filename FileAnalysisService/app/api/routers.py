# app/api/routers.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.repositories import SQLAnalysisRepository
from app.infrastructure.http_gateway import APIGatewayFileProvider
from app.use_cases.analyze_text import AnalyzeTextUseCase
from app.infrastructure.database import get_db

router = APIRouter()

@router.post("/analyze")
async def analyze(file_id: str, db: Session = Depends(get_db)):
    try:
        repo = SQLAnalysisRepository(db)
        provider = APIGatewayFileProvider()
        use_case = AnalyzeTextUseCase(provider, repo)
        analysis_id = await use_case.execute(file_id)
        return {"analysis_id": analysis_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/analyze/{analysis_id}")
def get_analysis(analysis_id: str, db: Session = Depends(get_db)):
    try:
        repo = SQLAnalysisRepository(db)
        stats = repo.get(analysis_id)
        return {
            "analysis_id": analysis_id,
            "word_count": stats.word_count,
            "char_count": stats.char_count,
            "paragraph_count": stats.paragraph_count
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
