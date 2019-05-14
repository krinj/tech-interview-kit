import unittest
from data_structures.python.graph import Graph, Vertex


class TestGraph(unittest.TestCase):

    def test_graph_add(self):
        """ We can add nodes. """
        graph = Graph()
        self.assertEqual(0, graph.vertex_count)
        self.assertEqual(None, graph.get_vertex("A"))

        graph.add_vertex("A", 155)
        self.assertEqual(1, graph.vertex_count)
        self.assertEqual(155, graph.get_vertex("A").data)

    def test_graph_directed(self):
        """ Check that we can created a directed or undirected graph. """
        graph = Graph()
        graph.add_edge("A", "B", directed=False)
        graph.add_edge("A", "C", directed=True)
        self.assertEqual(3, graph.vertex_count)
        self.assertEqual(3, graph.edge_count)
        self.assertTrue(graph.is_adjacent("A", "B"))
        self.assertTrue(graph.is_adjacent("B", "A"))
        self.assertTrue(graph.is_adjacent("A", "C"))
        self.assertFalse(graph.is_adjacent("C", "A"))

        graph.remove_edge("B", "A", directed=True)
        self.assertEqual(2, graph.edge_count)

        graph.add_edge("A", "B", directed=False)
        self.assertEqual(3, graph.edge_count)

        graph.remove_edge("B", "A", directed=False)
        self.assertEqual(1, graph.edge_count)

    def test_graph_adjacency(self):
        """ Test the adjacent properties and functions of the graph. """
        graph = Graph(directed=False)
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("A", "D")
        graph.add_edge("D", "E")
        graph.add_vertex("X")

        neighbors = graph.get_adjacent_keys("A")
        self.assertEqual(2, len(neighbors))
        self.assertTrue("D" in neighbors)
        self.assertTrue("B" in neighbors)

        neighbors = graph.get_adjacent_keys("D")
        self.assertEqual(2, len(neighbors))
        self.assertTrue("A" in neighbors)
        self.assertTrue("E" in neighbors)

        neighbors = graph.get_adjacent_keys("X")
        self.assertEqual(0, len(neighbors))

        self.assertTrue(graph.is_adjacent("A", "B"))
        self.assertTrue(graph.is_adjacent("B", "C"))
        self.assertFalse(graph.is_adjacent("A", "C"))

    def test_graph_edges(self):
        """ We add edges. Removing a vertex will also remove all connected edges. """
        graph = Graph()

        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("A", "C")

        self.assertEqual(3, graph.vertex_count)
        self.assertEqual(3, graph.edge_count)

        graph.remove_vertex("B")
        self.assertEqual(2, graph.vertex_count)
        self.assertEqual(1, graph.edge_count)

    def test_display(self):
        """ Test that we can nicely display the graph. """
        graph = Graph(directed=False)
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("A", "D")
        graph.add_edge("D", "E")
        graph.add_vertex("X")

        graph.display()

    def test_edge_weight(self):
        graph = Graph(directed=False)
        graph.add_edge("A", "B", 5)
        graph.add_edge("B", "C", 12)
        self.assertEqual(5, graph.get_edge_weight("B", "A"))
        self.assertEqual(12, graph.get_edge_weight("B", "C"))

    def test_graph_indexer(self):
        """ Test overridden index operators. """
        graph = Graph(directed=False)
        graph["A"] = 123
        graph["B"] = 456
        graph["C"] = 789
        graph["A"] = 555

        self.assertEqual(3, graph.vertex_count)
        self.assertEqual(555, graph["A"])
        self.assertEqual(456, graph["B"])
        self.assertEqual(789, graph["C"])

    def test_graph_iter(self):
        """ Test Graph Iterators. """
        graph = Graph(directed=False)
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("A", "D")
        graph.add_edge("D", "E")
        graph.add_vertex("X")

        i = 0
        vertex_keys = set()
        vertex_keys.add("A")
        vertex_keys.add("B")
        vertex_keys.add("C")
        vertex_keys.add("D")
        vertex_keys.add("E")
        vertex_keys.add("X")

        for k, v in graph:
            i += 1
            self.assertEqual(Vertex, type(v))
            vertex_keys.remove(k)

        self.assertEqual(6, i)
        self.assertEqual(0, len(vertex_keys))
