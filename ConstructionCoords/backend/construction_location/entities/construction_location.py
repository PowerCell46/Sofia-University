from database import Base
import uuid
from sqlalchemy import Column, Double, UUID


class ConstructionLocation(Base):
    __tablename__ = "constructions_locations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    # TODO: user_identifier (MAC address/optional name field)
    latitude = Column(Double, nullable=False)
    longitude = Column(Double, nullable=False)
