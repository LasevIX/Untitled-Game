from typing import Literal
import pygame as pg
import objects as o


def render_tilemap(
    tilemap: o.tileMap,
    surface: pg.surface.Surface,
    view_pos_on_map: tuple[int, int],
    view_pos_on_surf: tuple[int, int] | Literal["center"],
    px_per_tile: int = 10,
):
    if view_pos_on_surf == "center":
        view_pos_on_surf = (int(surface.get_width() / 2), int(surface.get_height() / 2))
