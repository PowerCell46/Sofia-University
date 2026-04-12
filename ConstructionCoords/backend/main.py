import uuid

from uuid import UUID as PyUUID
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, Column, Integer, String, Double, UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel, field_validator, ValidationError


app: FastAPI = FastAPI(title="ConstructionCoords Backend application")
# TODO: Add base path /api


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class ConstructionLocation(Base):
    __tablename__ = "constructions_locations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # user_identifier
    latitude = Column(Double, nullable=False)
    longitude = Column(Double, nullable=False)


Base.metadata.create_all(engine)


class CreateConstructionLocation(BaseModel):
    latitude: float
    longitude: float

    @classmethod
    @field_validator("latitude")
    def validate_latitude(cls, value):
        if not -90 <= value <= 90:
            raise ValueError("Latitude must be between -90 and 90 degrees.")
        return value

    @classmethod
    @field_validator("longitude")
    def validate_longitude(cls, value):
        if not -180 <= value <= 180:
            raise ValueError("Longitude must be between -180 and 180 degrees.")
        return value


class ResponseConstructionLocation(BaseModel):
    id: PyUUID
    latitude: float
    longitude: float


def get_db():
    db = SessionLocal()
    try:
        yield db  # Hands the session to the route, then resumes here after the route completes
    finally:
        db.close()

# TODO: Add logging


@app.post("/construction-location", response_model=ResponseConstructionLocation)
def persist_construction_location(req_construction_location: CreateConstructionLocation, db: Session = Depends(get_db)):
    db_construction_location = ConstructionLocation(**req_construction_location.model_dump())

    db.add(db_construction_location)
    db.commit()
    db.refresh(db_construction_location)

    return db_construction_location

# TODO: Endpoint for fetching all entries


@app.exception_handler(ValidationError)
async def handle_validation_error(request: Request, ex: ValidationError):
    return JSONResponse(status_code=422, content={"message": ex.errors()})


@app.exception_handler(HTTPException)
async def handle_http_exception(request: Request, ex: HTTPException):
    return JSONResponse(status_code=ex.status_code, content={"message": ex.detail})


@app.exception_handler(Exception)
async def handle_general_exception(request: Request, ex: Exception):
    # TODO: Log the error!
    return JSONResponse(status_code=500, content={"message": "Internal server error."})
