from typing import Literal
import pygame as pg
import objects as o

FLOOR_SIZE = FLOOR_WIDTH, FLOOR_HEIGHT = 720, 400


def render(
    tilemap: o.tileMap,
    surface: pg.surface.Surface,
    view_pos_on_map: tuple[int, int],
    view_pos_on_surf: tuple[int, int] | Literal["center"],
    px_per_tile: int = 10,
):
    if view_pos_on_surf == "center":
        view_pos_on_surf = (int(surface.get_width() / 2), int(surface.get_height() / 2))
    tile_amount = (
        round(surface.get_width() / px_per_tile),
        round(surface.get_height() / px_per_tile),
    )
    mapslice: o.tileMap = tilemap.get_tile_view(
        x=view_pos_on_map[0],
        y=view_pos_on_map[1],
        width=tile_amount[0],
        height=tile_amount[1],
    )
    for i,col in enumerate(mapslice._maparray):
        for j,tile in enumerate(col):
            rect_to_blit=pg.rect.Rect(i*px_per_tile,j*px_per_tile,px_per_tile,px_per_tile)
