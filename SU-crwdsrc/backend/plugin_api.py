from dataclasses import dataclass
from typing import Callable, Protocol, Iterator
from sqlalchemy.orm import Session, DeclarativeMeta
from fastapi import FastAPI


@dataclass
class PluginContext:
    base_class: DeclarativeMeta
    get_db: Callable[[], Iterator[Session]]


class Plugin(Protocol):
    def register(self, app: FastAPI, ctx: PluginContext) -> None:
        ...
