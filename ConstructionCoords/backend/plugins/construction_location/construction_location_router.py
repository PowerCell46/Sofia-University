import logging

from fastapi import APIRouter, Depends, HTTPException, Query
from geojson_pydantic import FeatureCollection, Feature, Point
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .dtos.request.create_construction_location_request_dto import CreateConstructionLocationRequestDTO
from .dtos.response.construction_location_geojson_response_dto import ConstructionLocationGeoJSONResponseDTO
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

    @router.get("", response_model=list[ConstructionLocationResponseDTO], status_code=200)
    def fetch_constructions_locations(page: int = Query(0, ge=0), size: int = Query(500, ge=1, le=1_000), db: Session = Depends(get_db)):
        constructions_locations = (
            db.query(ConstructionLocation)
            .offset(page * size)
            .limit(size)
            .all()
        )
        return constructions_locations

    # Visualize in browser geojson: https://geojson.io/
    @router.get("/geojson", response_model=FeatureCollection[Feature[Point, ConstructionLocationGeoJSONResponseDTO]], status_code=200)
    def fetch_constructions_locations_as_geojson(page: int = Query(0, ge=0), size: int = Query(500, ge=1, le=1_000), db: Session = Depends(get_db)):
        constructions_locations = (
            db.query(ConstructionLocation)
            .offset(page * size)
            .limit(size)
            .all()
        )

        point_features = []
        for construction_location in constructions_locations:
            current_feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [construction_location.longitude, construction_location.latitude]
                },
                "properties": {
                    "id": construction_location.id,
                    "created_at": construction_location.created_at,
                    "name": construction_location.name,
                    "name_confidence": construction_location.name_confidence,
                    "marker-symbol": "building",
                }
            }
            point_features.append(current_feature)

        return {
            "type": "FeatureCollection",
            "features": point_features
        }

    return router
