import logging

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from construction_location.dtos.request.create_construction_location_request_dto import CreateConstructionLocationRequestDTO
from construction_location.dtos.response.construction_location_response_dto import ConstructionLocationResponseDTO
from construction_location.entities.construction_location import ConstructionLocation
from database import get_db


logger: logging.Logger = logging.getLogger("app.routes.construction_location")
router: APIRouter = APIRouter(prefix="/api/construction-location")


@router.post("", response_model=ConstructionLocationResponseDTO, status_code=201)
def persist_construction_location(request_data: CreateConstructionLocationRequestDTO, db: Session = Depends(get_db)):
    logger.info("Creating construction location: lat=%s, lng=%s", request_data.latitude, request_data.longitude)

    db_construction_location: ConstructionLocation = ConstructionLocation(**request_data.model_dump())

    try:
        db.add(db_construction_location)
        db.commit()
        db.refresh(db_construction_location)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Invalid persistence state.")

    return db_construction_location


@router.get("", response_model=list[ConstructionLocationResponseDTO], status_code=200)
def fetch_constructions_locations(page: int = Query(0, ge=0), size: int = Query(500, ge=1, le=1_000), db: Session = Depends(get_db)):
    constructions_locations: list[ConstructionLocation] = (
        db.query(ConstructionLocation)
        .offset(page * size)
        .limit(size)
        .all()
    )
    return constructions_locations
