import pygame as pg
from pygame import locals as lc
import objects as o
import logic as l
import ceiling_rendering as cr
import sys
l.log(l.INFO,"main: Starting execution, imports complete")
SCREENSIZE=SCREENWIDTH,SCREENHEIGHT=720,480

done=False
pg.init()
DISPLAYSURF: pg.surface.Surface = pg.display.set_mode(SCREENSIZE)
fps=pg.time.Clock()
while not done:
    DISPLAYSURF.fill("#1d1d1d")
    for event in pg.event.get():
        if event.type == lc.QUIT:
            l.log(l.INFO,"process ended with code",lc.QUIT)
            pg.quit()
            sys.exit()

    pg.display.update()
    fps.tick(60)