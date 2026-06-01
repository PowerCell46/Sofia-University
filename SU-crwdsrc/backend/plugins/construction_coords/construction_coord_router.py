import logging

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .dtos.request.create_construction_coord_request_dto import CreateConstructionCoordRequestDTO
from .dtos.response.construction_coord_response_dto import ConstructionCoordResponseDTO


logger: logging.Logger = logging.getLogger("app.routes.construction_coord")


def build_router(get_db, ConstructionCoord) -> APIRouter:
    router: APIRouter = APIRouter(prefix="/api/construction-coords")

    @router.post("", response_model=ConstructionCoordResponseDTO, status_code=201)
    def persist_construction_coord(request_data: CreateConstructionCoordRequestDTO, db: Session = Depends(get_db)):
        logger.info("Creating construction coord: lat=%s, lng=%s", request_data.latitude, request_data.longitude)

        db_construction_coord = ConstructionCoord(**request_data.model_dump())

        try:
            db.add(db_construction_coord)
            db.commit()
            db.refresh(db_construction_coord)
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=409, detail="Invalid persistence state.")

        return db_construction_coord

    @router.get("", response_model=list[ConstructionCoordResponseDTO], status_code=200)
    def fetch_construction_coords(page: int = Query(0, ge=0), size: int = Query(500, ge=1, le=1_000), db: Session = Depends(get_db)):
        construction_coords = (
            db.query(ConstructionCoord)
            .offset(page * size)
            .limit(size)
            .all()
        )
        return construction_coords

    return router
