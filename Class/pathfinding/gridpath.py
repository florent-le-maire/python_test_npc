from Class.pathfinding.node import Node


class GridPath:
    def __init__(self, canvas, height, width):
        self.width_screen = int(canvas['width'])
        self.height_screen = int(canvas['height'])
        self.canvas = canvas
        self.nodes = []
        self.width = width
        self.height = height
        for x in range(height):
            for y in range(width):
                pos_x = x * (self.width_screen / self.width)
                pos_y = y * (self.height_screen / self.height)
                self.nodes.append(Node(pos_x, pos_y))
                print(pos_x, pos_y)



    def get_middle_node(self):
        middle_node_index = round((len(self.nodes) - 1) / 2)
        return self.nodes[int(middle_node_index)]

    def neighbors(self, node_search: Node):
        neighbors = []
        for i, node in enumerate(self.nodes):
            if len(neighbors) >= 8:
                break
            if node_search.is_neighbor(node):
                neighbors.append(node)
        return neighbors

    def cost(self, from_node, to_node):
        for i, j in self.nodes:
            if i == from_node and j == to_node:
                return 1
        return float('inf')

    def display_grid(self):
        for node in self.nodes:
            self.canvas.create_line(node.x, 0, node.x, self.width_screen, fill="black", width=1)
            self.canvas.create_line(0, node.y, self.height_screen, node.y, fill="black", width=1)
