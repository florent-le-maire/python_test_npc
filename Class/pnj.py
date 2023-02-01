import random


class PNJ:
    width = 25
    height = 25
    posX = 0
    posY = 0
    dX = 0
    dy = 0
    sprite = 0

    def __init__(self,posX,posY):
        self.posX = posX
        self.posY = posY
        self.height = self.height/2
        self.width = self.width/2
        self.sprite = 0

    def random_move(self):
        return random.randint(-1, 1)

    def affect_sprite(self,spriteID):
        self.sprite = spriteID
