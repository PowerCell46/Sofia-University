from fastapi import FastAPI

from plugin_api import PluginContext
from .entities.gym_node import build_entity
from .gym_node_router import build_router
from plugins.gym_nodes.utils.location_metadata_resolver import LocationMetadataResolver


def register(app: FastAPI, ctx: PluginContext) -> None:
    GymNode = build_entity(ctx.base_class)
    location_metadata_resolver: LocationMetadataResolver = LocationMetadataResolver()
    app.include_router(build_router(ctx.get_db, GymNode, location_metadata_resolver))
