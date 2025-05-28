# schemas
from pydantic import BaseModel

class FileUploadRequest(BaseModel):
    filename: str

class FileUploadResponse(BaseModel):
    file_id: str

