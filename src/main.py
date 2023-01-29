import pygame as pg
from pygame import locals as lc
import objects as o
import logic as l
import ceiling_rendering as cr
import floor_rendering as fr
import sys
l.log(l.INFO,"main: Starting execution, imports complete")
SCREENSIZE=SCREENWIDTH,SCREENHEIGHT=720,480

done=False
pg.init()
DISPLAYSURF: pg.surface.Surface = pg.display.set_mode(SCREENSIZE)
fps=pg.time.Clock()
r=pg.rect.Rect((0,0,720,400))
FLOORSURF=DISPLAYSURF.subsurface(r)
tm=o.tileMap(size=(16,9))

while not done:
    DISPLAYSURF.fill("#000000")
    for event in pg.event.get():
        if event.type == lc.QUIT:
            l.log(l.INFO,"process ended with code",lc.QUIT)
            pg.quit()
            sys.exit()
    fr.render(tm,FLOORSURF,(8,5),"center")
    pg.display.update()
    fps.tick(60)
    