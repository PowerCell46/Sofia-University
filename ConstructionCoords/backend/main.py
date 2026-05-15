import logging

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError
from starlette.responses import JSONResponse

from database import Base, engine, get_db
from plugin_api import PluginContext
from plugins import construction_location

PLUGINS = [construction_location]


logger: logging.Logger = logging.getLogger("app")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

app: FastAPI = FastAPI(title="ConstructionCoords Backend application")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

ctx = PluginContext(base_class=Base, get_db=get_db)
for plugin in PLUGINS:
    plugin.register(app, ctx)

# Creates DB tables for all imported models that extend Base (must run after model imports)
Base.metadata.create_all(engine)


@app.exception_handler(ValidationError)
async def handle_validation_exception(request: Request, ex: ValidationError):
    return JSONResponse(status_code=422, content={"message": ex.errors()})


@app.exception_handler(HTTPException)
async def handle_http_exception(request: Request, ex: HTTPException):
    return JSONResponse(status_code=ex.status_code, content={"message": ex.detail})


@app.exception_handler(IntegrityError)
async def handle_integrity_exception(request: Request, ex: IntegrityError):
    logger.error("Handling Integrity exception.", exc_info=True)
    return JSONResponse(status_code=500, content={"message": "Invalid persistence state."})


@app.exception_handler(Exception)
async def handle_general_exception(request: Request, ex: Exception):
    logger.error("Handling Unhandled exception.", exc_info=True)
    return JSONResponse(status_code=500, content={"message": "Internal server error."})
