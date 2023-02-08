import random

from Class.pathfinding.node import Node


class Npc:
    def __init__(self, canvas, pos: Node):
        self.canvas = canvas
        self.width = 25
        self.height = 25
        self.x = pos.x - self.width / 2
        self.y = pos.y - self.height / 2
        self.sprite = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="red")
        self.speed = 5

    def move(self):
        self.canvas.move(self.sprite, random.uniform(-self.speed, self.speed), random.uniform(-self.speed, self.speed))
