import unittest

from data_structures.python.graph_adj import GraphAdj


class TestGraphAdj(unittest.TestCase):

    def test_graph_adj(self):
        graph = GraphAdj()
        graph.add_vertex("A")
        graph.add_edge("A", "B")
        graph.add_edge("C", "D")
        graph.add_edge("D", "E")
        graph.remove_vertex("E")
        graph.display()
