from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ConstructionLocationResponse(BaseModel):
    id: UUID
    latitude: float
    longitude: float

    model_config = ConfigDict(from_attributes=True)
