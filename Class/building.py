class Building:
    def __init__(self, canvas, x, y, height, width, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.sprite = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,
                                                   fill=self.color)
