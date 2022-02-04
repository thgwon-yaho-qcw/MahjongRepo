from pydantic import BaseModel

from src.enum.common import CallType
from src.schema.tile import Tile


class Call(BaseModel):
    called_tile: Tile
    call_type: CallType
    other_tiles: list[Tile]
