from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class GymNodeGeoJSONResponseDTO(BaseModel):
    id: UUID
    created_at: datetime
    name: str
    name_confidence: float
    description: str
    marker_symbol: str = Field("building", alias="fitness-centre")
