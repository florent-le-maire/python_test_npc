import random

from Class.pathfinding.gridpath import GridPath
from Class.pathfinding.node import Node


class Npc:
    def __init__(self, canvas, pos: Node):
        self.canvas = canvas
        self.width = 25
        self.height = 25
        self.node_pos = pos
        self.x = 0
        self.y = 0
        self.get_pos_sprite()
        self.sprite = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="red")
        self.speed = 5

    def get_pos_sprite(self):
        self.x = self.node_pos.x - self.width / 2
        self.y = self.node_pos.y - self.height / 2

    def move(self, grid: GridPath):
        list_pos = grid.neighbors(Node(self.node_pos.x, self.node_pos.y))
        self.node_pos = list_pos[random.randint(0, len(list_pos) - 1)]
        self.get_pos_sprite()
        self.canvas.moveto(self.sprite, self.x, self.y)
