from Class.map import Map
from Class.npc import Npc
from Class.building import Building
import tkinter as tk
from tkinter import *


class GameManager:

    def __init__(self, screen_width, screen_height, refresh_time):
        # Const
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.SPAWN_POINT_X = self.SCREEN_WIDTH / 2
        self.SPAWN_POINT_Y = self.SCREEN_HEIGHT / 2
        self.REFRESH_TIME = refresh_time

        # Variable
        self.list_npc = []
        self.list_building = []
        self.is_running = True

        # Tkinter
        self.tk = Tk()

        # Jobs
        self.game_loop_job = 0

        # Game Map
        self.map_game = Map(self.tk, self.SCREEN_HEIGHT, self.SCREEN_WIDTH)
        self.map_game.create_center(600)

        self.create_ui()

        self.tk.mainloop()

    def play_game(self):
        self.generate_building(3)
        self.generate_npc(3)
        self.game_loop()

    # TODO create input number to choose how many npc do you want
    # TODO create stop simulation who erase current canvas
    def create_ui(self):
        start_button = tk.Button(self.tk, text="Start", command=self.play_game)
        start_button.pack()
        stop_button = tk.Button(self.tk, text="Pause/Play", command=self.stop_callback)
        stop_button.pack()
        quit_button = tk.Button(self.tk, text="Quitter", command=self.tk.destroy)
        quit_button.pack()

    def generate_npc(self, number):
        for i in range(number):
            self.list_npc.append(Npc(self.map_game.canvas, self.SPAWN_POINT_X, self.SPAWN_POINT_Y))

    # TODO update this function so that
    # TODO it can create a defined number of buildings
    def generate_building(self, number):
        tavern = Building(self.map_game.canvas, 600, 300, 100, 150, "blue")
        farm1 = Building(self.map_game.canvas, 60, 500, 50, 100, "grey")
        farm2 = Building(self.map_game.canvas, 1000, 500, 50, 100, "grey")

    def move(self):
        for npc in self.list_npc:
            npc.move()

    def stop_callback(self):
        if self.is_running:
            self.is_running = False
        else:
            self.is_running = True

    def game_loop(self):
        if self.is_running:
            self.move()
        self.game_loop_job = self.tk.after(self.REFRESH_TIME, self.game_loop)
