from fastapi import FastAPI

from plugin_api import PluginContext
from .entities.construction_location import build_entity
from .construction_location_router import build_router
from .location_name_resolver import LocationNameResolver


def register(app: FastAPI, ctx: PluginContext) -> None:
    ConstructionLocation = build_entity(ctx.base_class)
    location_name_resolver: LocationNameResolver = LocationNameResolver()
    app.include_router(build_router(ctx.get_db, ConstructionLocation, location_name_resolver))
