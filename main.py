from Class.map import Map
from Class.pnj import PNJ
import random

pnjs = []
for i in range(10):
    pnjs.append(PNJ(1280/2, 720/2))

map = Map(pnjs)


