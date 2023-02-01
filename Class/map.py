import time
from tkinter import *
from tkinter import ttk
from Class.pnj import PNJ


class Map:
    canvas = 0
    canvasWidth = 1280
    canvasHeight = 720
    canvasCircle = 300
    root = 0
    npcs = []
    npcSprite = [10]

    def __init__(self, npcs):
        self.root = Tk()

        # creating a simple canvas
        self.canvas = Canvas(self.root, bg="white", height=str(self.canvasHeight), width=str(self.canvasWidth))
        self.canvas.pack()
        self.canvas.create_oval(self.canvasWidth / 2 - self.canvasCircle, self.canvasHeight / 2 - self.canvasCircle,
                                self.canvasWidth / 2 + self.canvasCircle, self.canvasHeight / 2 + self.canvasCircle,
                                outline="blue")
        self.npcs = npcs
        for npc in self.npcs:
            self.pnj_sprite(npc)

        self.root.after(75, self.draw)

        self.root.mainloop()

    def draw(self):
        # self.canvas.delete("all")
        self.move()
        self.root.after(75, self.draw)
        # time.sleep(0.01)

    def move(self):
        for npc in self.npcs:
            self.canvas.move(npc.sprite,npc.random_move(), npc.random_move())

    def pnj_sprite(self, npc: PNJ):
        npc.affect_sprite(self.canvas.create_rectangle(npc.posX - npc.width, npc.posY - npc.height, npc.posX + npc.width,
                                         npc.posY + npc.height, fill='red', outline='red'))
