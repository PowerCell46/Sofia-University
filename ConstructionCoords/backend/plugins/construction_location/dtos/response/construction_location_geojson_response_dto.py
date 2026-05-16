from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class ConstructionLocationGeoJSONResponseDTO(BaseModel):
    id: UUID
    created_at: datetime
    name: str
    name_confidence: float
    marker_symbol: str = Field("building", alias="marker-symbol")
