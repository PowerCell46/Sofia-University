from fastapi import FastAPI

from plugin_api import PluginContext
from .entities.construction_coord import build_entity
from .construction_coord_router import build_router


def register(app: FastAPI, ctx: PluginContext) -> None:
    ConstructionCoord = build_entity(ctx.base_class)
    app.include_router(build_router(ctx.get_db, ConstructionCoord))
