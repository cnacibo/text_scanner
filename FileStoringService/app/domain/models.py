# FileStoringService/app/models.py
from sqlalchemy import Column, String, UUID
from ..infrastructure.database import Base

class File(Base):
    __tablename__ = 'files'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    filename = Column(String, nullable=False)
    location = Column(String, nullable=False)