# FileAnalysisService/app/main.py
from fastapi import FastAPI
from app.api.routers import router  # Изменили импорт
from app.infrastructure.database import Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8001)