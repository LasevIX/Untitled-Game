import pygame as pg
from pygame import locals as lc
import objects as o
import logic as l
l.log(l.INFO,"main: Starting execution, imports complete")
SCREENSIZE=SCREENWIDTH,SCREENHEIGHT=480,720

done=False
pg.init()
DISPLAYSURF = pg.display.set_mode(SCREENSIZE)
fps=pg.time.Clock()
while not done:
        fps.tick(60)