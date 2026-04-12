import logging

from fastapi import FastAPI, HTTPException, Request
from pydantic import ValidationError
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from construction_location.construction_location_router import router as construction_location_router
from database import Base, engine


Base.metadata.create_all(engine)

logger: logging.Logger = logging.getLogger("app")
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)-8s | %(message)s") # TODO: Make it more beautifully formated

app: FastAPI = FastAPI(title="ConstructionCoords Backend application")

app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],
      allow_methods=["*"],
      allow_headers=["*"],
  )

app.include_router(construction_location_router)


@app.exception_handler(ValidationError)
async def handle_validation_error(request: Request, ex: ValidationError):
    return JSONResponse(status_code=422, content={"message": ex.errors()})


@app.exception_handler(HTTPException)
async def handle_http_exception(request: Request, ex: HTTPException):
    return JSONResponse(status_code=ex.status_code, content={"message": ex.detail})


# TODO: handle IntegrityError or at least SQLAlchemyError


@app.exception_handler(Exception)
async def handle_general_exception(request: Request, ex: Exception):
    logger.error("Unhandled exception", exc_info=True)
    return JSONResponse(status_code=500, content={"message": "Internal server error."})
