from fastapi import FastAPI

from plugin_api import PluginContext
from .entities.geo_ai_point import build_entity
from .geo_ai_point_router import build_router
from plugins.geo_ai.utils.location_metadata_resolver import LocationMetadataResolver


def register(app: FastAPI, ctx: PluginContext) -> None:
    GeoAiPoint = build_entity(ctx.base_class)
    location_metadata_resolver: LocationMetadataResolver = LocationMetadataResolver()
    app.include_router(build_router(ctx.get_db, GeoAiPoint, location_metadata_resolver))
