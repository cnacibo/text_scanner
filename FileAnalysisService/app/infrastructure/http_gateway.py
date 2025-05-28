# app/infrastructure/http_gateway.py
import httpx
from app.domain.interfaces import FileContentProvider

class APIGatewayFileProvider(FileContentProvider):
    async def get_content(self, file_id: str) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://api-gateway:8000/files/{file_id}/content")
            response.raise_for_status()
            return response.json()["content"]
