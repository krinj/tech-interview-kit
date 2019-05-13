class GraphAdj:

    # Graph using adjacency list implementation.
    # The graph will use a key as node id.
    # The key will be used as a map index to a list of connected keys.

    # Vertices Represented as a Set.
    # Edges Represented as a List.

    def __init__(self):
        self.vertices = set()
        self.edges = []

    def add_edge(self, x, y):
        """ Add an edge from x to y. """
        self.vertices.add(x)
        self.vertices.add(y)

        edge = (x, y)
        if edge not in self.edges:
            self.edges.append(edge)

    def vertex_count(self):
        return len(self.vertices)

    def edge_count(self):
        return len(self.edges)

    def add_vertex(self, x):
        self.vertices.add(x)

    def remove_vertex(self, x):
        self.vertices.remove(x)
        for i in range(len(self.edges) - 1, -1, -1):
            edge = self.edges[i]
            if x in edge:
                self.edges.pop(i)

    def remove_edge(self, x, y):
        edge = (x, y)
        if edge in self.edges:
            self.edges.remove(edge)

    def display(self):
        """ Display all edges and weight directions. """
        if len(self.vertices) == 0:
            print("--- No Vertices ---")
        else:
            print(f"Verticies: {list(self.vertices)}")

        if len(self.edges) == 0:
            print("--- No Edges ---")
        else:
            print("--- Edges ---")
            for edge in self.edges:
                print(f"{edge[0]} -> {edge[1]}")
