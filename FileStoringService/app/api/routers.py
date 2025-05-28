# app/api/routers.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.infrastructure.local_storage import LocalFileStorage
from app.infrastructure.text_extractor import TextractTextExtractor
from app.use_cases.save_file import SaveFileUseCase
from app.use_cases.extract_text import ExtractTextUseCase
from app.infrastructure.repositories import FileRepository
from fastapi import Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from uuid import UUID
from fastapi import Path
import logging
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/files")
async def upload(file: UploadFile = File(...), db: Session = Depends(get_db)):
    logger.info("Upload file called")
    try:
        content = await file.read()
        storage = LocalFileStorage()
        repo = FileRepository(db)
        use_case = SaveFileUseCase(storage, repo, db)
        file_id = use_case.execute(file.filename, content)
        return {"file_id": file_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/files/{file_id}")
def get_file_metadata(file_id: UUID = Path(...), db: Session = Depends(get_db)):
    repo = FileRepository(db)
    file = repo.get_by_id(file_id)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    return {"file_id": file.id, "filename": file.filename}

@router.get("/files/{file_id}/content")
def get_content(file_id: str, db: Session = Depends(get_db)):
    try:
        storage = LocalFileStorage()
        extractor = TextractTextExtractor()
        repo = FileRepository(db)
        use_case = ExtractTextUseCase(storage, extractor, repo, db)
        text = use_case.execute(file_id)
        return {"content": text}
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise

