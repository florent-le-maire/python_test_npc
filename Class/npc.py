import random


class Npc:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.width = 25
        self.height = 25
        self.x = x - self.width / 2
        self.y = y - self.height / 2
        self.sprite = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="red")
        self.speed = 5

    def move(self):
        self.canvas.move(self.sprite, random.uniform(-self.speed, self.speed), random.uniform(-self.speed, self.speed))
