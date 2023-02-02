from Class.map import Map
from Class.npc import Npc
from Class.building import Building
import tkinter as tk

# Constante
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SPAWN_POINT_X = SCREEN_WIDTH / 2
SPAWN_POINT_Y = SCREEN_HEIGHT / 2
REFRESH_TIME = 100

# Variable
list_npc = []
is_running = True


def move():
    for npc in list_npc:
        npc.move()


def stop_callback():
    global is_running
    if is_running:
        is_running = False
    else:
        is_running = True


def game_loop():
    print(is_running)
    if is_running:
        move()
    map_game.tk.after(REFRESH_TIME, game_loop)


if __name__ == '__main__':
    map_game = Map(SCREEN_HEIGHT, SCREEN_WIDTH)

    map_game.create_center(600)

    tavern = Building(map_game.canvas, 600, 300, 100, 150, "blue")
    farm1 = Building(map_game.canvas, 60, 500, 50, 100, "grey")
    farm2 = Building(map_game.canvas, 1000, 500, 50, 100, "grey")

    for i in range(10):
        list_npc.append(Npc(map_game.canvas, SPAWN_POINT_X, SPAWN_POINT_Y))

    stop_button = tk.Button(map_game.tk, text="Pause/Play", command=stop_callback)
    stop_button.pack()

    game_loop()

    map_game.tk.mainloop()
