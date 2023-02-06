class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return '({0}, {1})'.format(self.x, self.y)

    def is_neighbor(self, other):
        if self == other:
            return False
        dif_x = self.x - other.x
        dif_y = self.y - other.y
        return 1 >= dif_x >= -1 and 1 >= dif_y >= -1
