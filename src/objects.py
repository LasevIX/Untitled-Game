from typing import Literal, Type
import pygame as pg


class Item:
    ceiling_sprite: pg.sprite.Sprite
    floor_sprite: pg.sprite.Sprite
    animations: list[
        tuple[str, list[tuple[str, str]]]
    ]  # floor & ceiling sprite filenames (empty if no animation)


class ConsumableItem(Item):
    def __init__(self) -> None:
        self.uses: int  # 0 if depends on something else like bullets
        self.cooldown: float  # -1 if it uses a different system


class WeaponItem(ConsumableItem):
    def __init__(self) -> None:
        self.uses = 0
        self.cooldown = -1
        self.animations = [("fire", []), ("reload", [])]


class BuffItem(ConsumableItem):
    pass


class FoodItem(BuffItem):
    pass


class WaterBottle(BuffItem):
    pass


class BuildItem(ConsumableItem):
    pass


class floorTile:
    player_collideable: bool
    sprite: pg.sprite.Sprite
    z_index: int


class emptyFloorTile(floorTile):
    pass


class tileFloorTile(floorTile):
    """a literal floor tile tile."""

    def __init__(self) -> None:
        self.player_collideable = False


class tileMap:
    def __init__(
        self, size: tuple[int, int] = (-1, -1), height: int = -1, width: int = -1
    ) -> None:
        if height < 0 or width < 0:
            if size[0] < 0 or size[1] < 0:
                raise ValueError
            else:
                self.height, self.width = size[0], size[1]
                self.size: tuple[int, int] = self.height, self.width
        else:
            self.size = self.height, self.width = height, width
        self._maparray: list[list[Type[emptyFloorTile]]] = [
            [emptyFloorTile for tile in range(self.height)]
            for column in range(self.width)
        ]

    def get_tile(self, x, y) -> floorTile:
        if not 0 < x < self.width or not 0 < y < self.height:
            raise ValueError
        return emptyFloorTile()

    def get_tile_view(self, x, y, height, width):

        return tileMap(height=height, width=width)
        pass
