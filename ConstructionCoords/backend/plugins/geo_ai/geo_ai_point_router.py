import logging

from fastapi import APIRouter, Depends, HTTPException, Query
from geojson_pydantic import FeatureCollection, Feature, Point
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .dtos.request.create_geo_ai_point_request_dto import CreateGeoAiPointRequestDTO
from .dtos.response.geo_ai_point_geojson_response_dto import GeoAiPointGeoJSONResponseDTO
from .dtos.response.geo_ai_point_response_dto import GeoAiPointResponseDTO
from plugins.geo_ai.utils.location_metadata_resolver import LocationMetadataResolver

logger: logging.Logger = logging.getLogger("app.routes.geo_ai")


def build_router(get_db, GeoAiPoint, location_metadata_resolver: LocationMetadataResolver) -> APIRouter:
    router: APIRouter = APIRouter(prefix="/api/geo-ai")

    @router.post("", response_model=GeoAiPointResponseDTO, status_code=201)
    def persist_geo_ai_point(request_data: CreateGeoAiPointRequestDTO, db: Session = Depends(get_db)):
        logger.info("Creating geo ai point: lat=%s, lng=%s", request_data.latitude, request_data.longitude)

        db_geo_ai_point = GeoAiPoint(**request_data.model_dump())
        location_metadata_resolver.annotate_location(db_geo_ai_point)

        try:
            db.add(db_geo_ai_point)
            db.commit()
            db.refresh(db_geo_ai_point)
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=409, detail="Invalid persistence state.")

        return db_geo_ai_point

    @router.get("", response_model=list[GeoAiPointResponseDTO], status_code=200)
    def fetch_geo_ai_points(page: int = Query(0, ge=0), size: int = Query(500, ge=1, le=1_000),
                            db: Session = Depends(get_db)):
        geo_ai_points = (
            db.query(GeoAiPoint)
            .offset(page * size)
            .limit(size)
            .all()
        )
        return geo_ai_points

    # Visualize in browser geojson: https://geojson.io/
    @router.get("/geojson", response_model=FeatureCollection[Feature[Point, GeoAiPointGeoJSONResponseDTO]], status_code=200)
    def fetch_geo_ai_points_as_geojson(page: int = Query(0, ge=0), size: int = Query(500, ge=1, le=1_000), db: Session = Depends(get_db)):
        geo_ai_points = (
            db.query(GeoAiPoint)
            .offset(page * size)
            .limit(size)
            .all()
        )

        point_features = []
        for geo_ai_point in geo_ai_points:
            current_feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [geo_ai_point.longitude, geo_ai_point.latitude]
                },
                "properties": {
                    "id": geo_ai_point.id,
                    "created_at": geo_ai_point.created_at,
                    "name": geo_ai_point.name,
                    "name_confidence": geo_ai_point.name_confidence,
                    "type": geo_ai_point.type,
                    "visibility_level": geo_ai_point.visibility_level,
                    "description": geo_ai_point.description,
                    "marker-symbol": "building",
                }
            }
            point_features.append(current_feature)

        return {
            "type": "FeatureCollection",
            "features": point_features
        }

    return router
