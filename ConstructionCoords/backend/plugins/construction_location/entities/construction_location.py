import uuid
from sqlalchemy import Column, Double, UUID, DateTime, func, String
from sqlalchemy.orm import DeclarativeMeta


def build_entity(Base: DeclarativeMeta) -> type:
    class ConstructionLocation(Base):
        __tablename__ = "constructions_locations"

        id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
        created_at = Column(DateTime(timezone=False), server_default=func.now(), nullable=False)
        latitude = Column(Double, nullable=False)
        longitude = Column(Double, nullable=False)
        name = Column(String, nullable=False, default="N/A")
        name_confidence = Column(Double, nullable=False, default=0.0)
        # user_identifier (MAC address/optional name field)

    return ConstructionLocation
