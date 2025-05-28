from pydantic import BaseModel

class FileUploadResponse(BaseModel):
    file_id: str

class FileMetadataResponse(BaseModel):
    file_id: str
    filename: str
    location: str
