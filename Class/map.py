import time
from tkinter import *
from tkinter import ttk
from Class.npc import Npc


class Map:
    def __init__(self, tk, canvas_height, canvas_width):
        self.height = canvas_height
        self.width = canvas_width
        # creating a simple canvas
        self.canvas = Canvas(tk, bg="white", height=str(canvas_height), width=str(canvas_width))
        self.canvas.pack()

    def create_center(self, circle_radius):
        circle_radius /= 2
        self.canvas.create_oval(self.width / 2 - circle_radius, self.height / 2 - circle_radius,
                                self.width / 2 + circle_radius, self.height / 2 + circle_radius,
                                outline="blue")
