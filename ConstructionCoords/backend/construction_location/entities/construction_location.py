from database import Base
import uuid
from sqlalchemy import Column, Double, UUID, DateTime, func


class ConstructionLocation(Base):
    __tablename__ = "constructions_locations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime(timezone=False), server_default=func.now(), nullable=False)
    latitude = Column(Double, nullable=False)
    longitude = Column(Double, nullable=False)
    # user_identifier (MAC address/optional name field)
