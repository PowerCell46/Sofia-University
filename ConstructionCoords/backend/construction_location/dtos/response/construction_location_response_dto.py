from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ConstructionLocationResponseDTO(BaseModel):
    id: UUID
    latitude: float
    longitude: float

    model_config = ConfigDict(from_attributes=True)
