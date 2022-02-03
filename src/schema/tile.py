from typing import Any

from pydantic import BaseModel, root_validator

from src.enum.common import TileType

TILE_TYPE_CNT = {
    TileType.MAN: 9,
    TileType.PIN: 9,
    TileType.SOU: 9,
    TileType.WIND: 4,
    TileType.DRAGON: 3,
}


class Tile(BaseModel):
    type: TileType
    value: int

    @root_validator
    def validate_tile(cls, values: dict[str, Any]):
        t, v = values["type"], values["value"]
        if v < 1 or v > TILE_TYPE_CNT[t]:
            raise ValueError("Not Exist Tile")
        return values
