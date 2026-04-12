import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from construction_location.dtos.request.create_construction_location_request import CreateConstructionLocationRequest
from construction_location.dtos.response.construction_location_response import ConstructionLocationResponse
from construction_location.entities.construction_location import ConstructionLocation
from database import get_db


logger = logging.getLogger("app.routes.construction_location")
router: APIRouter = APIRouter(prefix="/api/construction-location")


@router.post("", response_model=ConstructionLocationResponse)
def persist_construction_location(request_data: CreateConstructionLocationRequest, db: Session = Depends(get_db)):
    logger.info("---> POST request on /api/construction-location.")

    db_construction_location = ConstructionLocation(**request_data.model_dump())

    db.add(db_construction_location)
    db.commit()
    db.refresh(db_construction_location)

    return db_construction_location

# TODO: Add endpoint for fetching all entries (called by the arcgis project
