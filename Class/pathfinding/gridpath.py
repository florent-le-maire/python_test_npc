from Class.pathfinding.node import Node


class GridPath:
    def __init__(self, height, width):
        self.nodes = []
        self.width = width
        self.height = height
        for i in range(height):
            for j in range(width):
                self.nodes.append(Node(i, j))

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

    def display_grid(self, canvas, width_screen, height_screen):
        print("c'est l'esprit de la scep")
