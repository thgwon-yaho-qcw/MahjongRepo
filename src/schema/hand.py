from typing import Optional

from pydantic import BaseModel

from src.schema.call import Call
from src.schema.tile import Tile


class Hand(BaseModel):
    tiles: list[Tile]
    calls: list[Call]
    draw_tile: Optional[Tile]
