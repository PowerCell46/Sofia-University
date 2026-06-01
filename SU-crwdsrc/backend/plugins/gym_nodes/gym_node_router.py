import logging

from fastapi import APIRouter, Depends, HTTPException, Query
from geojson_pydantic import FeatureCollection, Feature, Point
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .dtos.request.create_gym_node_request_dto import CreateGymNodeRequestDTO
from .dtos.response.gym_node_geojson_response_dto import GymNodeGeoJSONResponseDTO
from .dtos.response.gym_node_response_dto import GymNodeResponseDTO
from plugins.gym_nodes.utils.location_metadata_resolver import LocationMetadataResolver

logger: logging.Logger = logging.getLogger("app.routes.gym_nodes")


def build_router(get_db, GymNode, location_metadata_resolver: LocationMetadataResolver) -> APIRouter:
    router: APIRouter = APIRouter(prefix="/api/gym-nodes")

    @router.post("", response_model=GymNodeResponseDTO, status_code=201)
    def persist_gym_node(request_data: CreateGymNodeRequestDTO, db: Session = Depends(get_db)):
        logger.info("Creating gym node: lat=%s, lng=%s", request_data.latitude, request_data.longitude)

        db_gym_node = GymNode(**request_data.model_dump())
        location_metadata_resolver.annotate_location(db_gym_node)

        try:
            db.add(db_gym_node)
            db.commit()
            db.refresh(db_gym_node)
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=409, detail="Invalid persistence state.")

        return db_gym_node

    @router.get("", response_model=list[GymNodeResponseDTO], status_code=200)
    def fetch_gym_nodes(page: int = Query(0, ge=0), size: int = Query(500, ge=1, le=1_000), db: Session = Depends(get_db)):
        gym_nodes = (
            db.query(GymNode)
            .offset(page * size)
            .limit(size)
            .all()
        )
        return gym_nodes

    # Visualize in browser geojson: https://geojson.io/
    @router.get("/geojson", response_model=FeatureCollection[Feature[Point, GymNodeGeoJSONResponseDTO]], status_code=200)
    def fetch_gym_nodes_as_geojson(page: int = Query(0, ge=0), size: int = Query(500, ge=1, le=1_000), db: Session = Depends(get_db)):
        gym_nodes = (
            db.query(GymNode)
            .offset(page * size)
            .limit(size)
            .all()
        )

        point_features = []
        for gym_node in gym_nodes:
            current_feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [gym_node.longitude, gym_node.latitude]
                },
                "properties": {
                    "id": gym_node.id,
                    "created_at": gym_node.created_at,
                    "name": gym_node.name,
                    "name_confidence": gym_node.name_confidence,
                    "description": gym_node.description,
                    "marker-symbol": "building",
                }
            }
            point_features.append(current_feature)

        return {
            "type": "FeatureCollection",
            "features": point_features
        }

    return router
