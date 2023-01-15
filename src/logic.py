import logging
from logging import INFO,WARNING,DEBUG,ERROR

logging.basicConfig(filename="game.log",format="%(asctime)s %(levelname)s :%(message)s")
log=logging.log