from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class GymNodeResponseDTO(BaseModel):
    id: UUID
    created_at: datetime
    latitude: float
    longitude: float
    name: str
    name_confidence: float
    description: str

    model_config = ConfigDict(from_attributes=True)
