from uuid import UUID

from pydantic import BaseModel


class ConstructionLocationResponse(BaseModel):
    id: UUID
    latitude: float
    longitude: float
