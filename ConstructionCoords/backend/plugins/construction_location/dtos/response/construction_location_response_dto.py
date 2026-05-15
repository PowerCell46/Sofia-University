from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ConstructionLocationResponseDTO(BaseModel):
    id: UUID
    created_at: datetime
    latitude: float
    longitude: float

    model_config = ConfigDict(from_attributes=True)
