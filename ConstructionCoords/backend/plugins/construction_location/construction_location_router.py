import logging

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .dtos.request.create_construction_location_request_dto import CreateConstructionLocationRequestDTO
from .dtos.response.construction_location_response_dto import ConstructionLocationResponseDTO
from .location_name_resolver import LocationNameResolver

logger: logging.Logger = logging.getLogger("app.routes.construction_location")


def build_router(get_db, ConstructionLocation, location_name_resolver: LocationNameResolver) -> APIRouter:
    router: APIRouter = APIRouter(prefix="/api/construction-location")

    @router.post("", response_model=ConstructionLocationResponseDTO, status_code=201)
    def persist_construction_location(request_data: CreateConstructionLocationRequestDTO, db: Session = Depends(get_db)):
        logger.info("Creating construction location: lat=%s, lng=%s", request_data.latitude, request_data.longitude)

        db_construction_location = ConstructionLocation(**request_data.model_dump())
        location_name_resolver.assign_name_to_point(db_construction_location)

        try:
            db.add(db_construction_location)
            db.commit()
            db.refresh(db_construction_location)
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=409, detail="Invalid persistence state.")

        return db_construction_location

    @router.get("", response_model=list[ConstructionLocationResponseDTO], status_code=200)  # TODO: Create new entity GeoJSON and return it here
    def fetch_constructions_locations(page: int = Query(0, ge=0), size: int = Query(500, ge=1, le=1_000), db: Session = Depends(get_db)):
        constructions_locations = (
            db.query(ConstructionLocation)
            .offset(page * size)
            .limit(size)
            .all()
        )
        return constructions_locations

    return router
