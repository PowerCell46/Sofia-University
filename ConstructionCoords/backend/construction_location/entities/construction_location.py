from database import Base
import uuid
from sqlalchemy import Column, Double, UUID


class ConstructionLocation(Base):
    __tablename__ = "constructions_locations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # TODO: user_identifier
    latitude = Column(Double, nullable=False)
    longitude = Column(Double, nullable=False)
