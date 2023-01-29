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


class floorTile(pg.sprite.Sprite):
    player_collideable: bool
    sprite: pg.sprite.Sprite
    z_index: int


class emptyFloorTile(floorTile):
    def __init__(self, *groups) -> None:
        super().__init__(*groups)
        self.image=pg.Surface((1,1))
        self.image.fill("#1d1d1d")
        self.surf=self.image
        self.rect=self.surf.get_rect()


class tileFloorTile(floorTile):
    """a literal floor tile tile."""

    def __init__(self) -> None:
        self.player_collideable = False


class tileMap:
    def __init__(
        self,
        size: tuple[int, int] = (-1, -1),
        height: int = -1,
        width: int = -1,
        maparray_to_use=None,
    ) -> None:
        if maparray_to_use is None:
            if height < 0 or width < 0:
                if size[0] < 0 or size[1] < 0:
                    raise ValueError
                else:
                    self.height, self.width = size[0], size[1]
                    self.size: tuple[int, int] = self.height, self.width
            else:
                self.size = self.height, self.width = height, width
            self._maparray: list[list[emptyFloorTile]] = [
                [emptyFloorTile() for tile in range(self.height)]
                for column in range(self.width)
            ]
        elif isinstance(maparray_to_use,list) and len(maparray_to_use)>0:
            self._maparray = maparray_to_use.copy()
            self.size = self.width, self.height = len(self._maparray), len(
                self._maparray[0]
            )
            print("MAP USED:",self._maparray)
        else: raise ValueError

    def get_tile(self, x, y) -> floorTile:  #TODO
        if not 0 < x < self.width or not 0 < y < self.height:
            raise ValueError
        return emptyFloorTile()

    def get_tile_view(self, x, y, height, width):
        arr: list[list[emptyFloorTile]] = [
            column[y : y + height] for column in self._maparray[x : x + width]
        ]
        print(type(arr), len(arr))
        return tileMap(maparray_to_use=arr)
