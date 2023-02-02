class Grid:
    def __init__(self, edges):
        self.edges = edges

    def neighbors(self, node):
        neighbors = []
        for i, j in self.edges:
            if i == node:
                neighbors.append(j)
        return neighbors

    def cost(self, from_node, to_node):
        for i, j in self.edges:
            if i == from_node and j == to_node:
                return 1
        return float('inf')

