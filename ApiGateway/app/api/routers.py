from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import httpx
from typing import Dict, Any

router = APIRouter()

# URL микросервисов
FILE_STORING_SERVICE = "http://file-storing:8002"
FILE_ANALYSIS_SERVICE = "http://file-analysis:8001"

async def make_service_request(
    method: str,
    service_url: str,
    endpoint: str,
    **kwargs
) -> Dict[str, Any]:
    url = f"{service_url}{endpoint}"
    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()


@router.post("/files", response_model=Dict[str, Any]) # загрузка файла
async def upload_file(file: UploadFile = File(...)) -> JSONResponse:
    file_content = await file.read()
    files_data = {"file": (file.filename, file_content)}

    response = await make_service_request(
        "POST",
        FILE_STORING_SERVICE,
        "/files",
        files=files_data
    )
    return JSONResponse(content=response)


@router.get("/files/{file_id}", response_model=Dict[str, Any]) # получение файла по id
async def get_file(file_id: str) -> JSONResponse:
    response = await make_service_request(
        "GET",
        FILE_STORING_SERVICE,
        f"/files/{file_id}"
    )
    return JSONResponse(content=response)


@router.get("/files/{file_id}/content", response_model=Dict[str, Any]) # получение содержимого файла по id
async def get_file_content(file_id: str) -> JSONResponse:
    response = await make_service_request(
        "GET",
        FILE_STORING_SERVICE,
        f"/files/{file_id}/content"
    )
    return JSONResponse(content=response)


@router.post("/analyze", response_model=Dict[str, Any]) # анализ содержимого файла по id файла
async def analyze_file(file_id: str) -> JSONResponse:
    response = await make_service_request(
        "POST",
        FILE_ANALYSIS_SERVICE,
        f"/analyze?file_id={file_id}"
    )
    return JSONResponse(content=response)


@router.get("/analyze/{analyze_id}", response_model=Dict[str, Any]) # получение анализа содержимого файла по id анализа
async def get_analyze_result(analyze_id: str) -> JSONResponse:
    response = await make_service_request(
        "GET",
        FILE_ANALYSIS_SERVICE,
        f"/analyze/{analyze_id}"
    )
    return JSONResponse(content=response)
