# -*- coding: utf-8 -*-

"""
A proper, full function graph implementation.
Implemented as references.
"""

from typing import Dict, List

__author__ = "Jakrin Juangbhanich"
__email__ = "juangbhanich.k@gmail.com"


class Vertex:
    def __init__(self, key: str, data=None):
        self.key = key
        self.data = data
        self.edges: Dict[key, float] = {}


class Graph:
    def __init__(self, directed: bool=True, default_weight: float=1):
        self._default_directed: bool = directed
        self._default_weight: float = default_weight
        self._vertex_map: Dict[str, Vertex] = {}
        self._n_edges = 0

    def add_vertex(self, key: str, data=None):
        """ Add a vertex to this graph. """
        if key in self._vertex_map:
            self._vertex_map[key].data = data
        else:
            v = Vertex(key, data)
            self._vertex_map[key] = v

    def get_vertex(self, key: str):
        if key in self._vertex_map:
            return self._vertex_map[key]
        else:
            return None

    def __getitem__(self, key):
        return self.get_vertex(key).data

    def __setitem__(self, key, data):
        return self.add_vertex(key, data)

    def remove_vertex(self, key):
        """ Remove a vertex from this graph. All connected edges will also be removed. """
        for k, v in self._vertex_map.items():
            if key in v.edges:
                v.edges.pop(key)
                self._n_edges -= 1

        self._n_edges -= len(self._vertex_map[key].edges)
        self._vertex_map.pop(key)

    def add_edge(self, key_from, key_to, weight: float=None, directed: bool=None):
        """ Add an edge to this graph. If the vertex is not in, it will create one. """

        if directed is None:
            directed = self._default_directed

        if weight is None:
            weight = self._default_weight

        if key_from not in self._vertex_map:
            self.add_vertex(key_from, None)

        if key_to not in self._vertex_map:
            self.add_vertex(key_to, None)

        v_from = self._vertex_map[key_from]
        if key_to not in v_from.edges:
            self._n_edges += 1
        v_from.edges[key_to] = weight

        if not directed:
            v_to = self._vertex_map[key_to]
            if key_from not in v_to.edges:
                self._n_edges += 1
            v_to.edges[key_from] = weight

    def remove_edge(self, key_from, key_to, directed: bool=None):
        """ Remove an edge from the graph. """
        if directed is None:
            directed = self._default_directed

        if key_from not in self._vertex_map:
            raise Exception

        v_from = self._vertex_map[key_from]
        v_from.edges.pop(key_to)

        if not directed:
            v_to = self._vertex_map[key_to]
            if key_from in v_to.edges:
                v_to.edges.pop(key_from)
                self._n_edges -= 1

        self._n_edges -= 1

    def is_adjacent(self, key1: str, key2: str):
        return key2 in self._vertex_map[key1].edges

    def get_adjacent(self, key: str) -> List[Vertex]:
        """ Get a list of all vertices reachable by the given key. """
        n_keys = self._vertex_map[key].edges.keys()
        vertices = [self._vertex_map[k] for k in n_keys]
        return vertices

    def get_adjacent_keys(self, key: str) -> List[str]:
        """ Get the keys of all the reachable vertices from the given vertex. """
        return [v.key for v in self.get_adjacent(key)]

    @property
    def vertex_count(self) -> int:
        """ Number of vertices in the graph. """
        return len(self._vertex_map)

    @property
    def edge_count(self) -> int:
        """ All edges in the graph. Undirected edges will count as two edges. """
        return self._n_edges

    def display(self):
        """ Print out the graph into the std::out. """
        print("\n--- GRAPH ---")
        print(f"\nVERTS: {self.vertex_count}")
        if self.vertex_count > 0:
            print(" ".join(self._vertex_map.keys()))

        print(f"\nEDGES: {self.edge_count }")
        if self.edge_count > 0:

            seen_map = {}  # Prevent undirected arrows being printed twice.

            for k, v in self._vertex_map.items():
                for k2, w in v.edges.items():

                    if k in seen_map and seen_map[k] == k2:
                        continue

                    v2 = self._vertex_map[k2]
                    if k in v2.edges and v2.edges[k] == w:
                        print(f"{k} <--{w}--> {k2}")
                        seen_map[k2] = k
                    else:
                        print(f"{k} ---{w}--> {k2}")

        print("")

    # ===================================================================================================
    # Iterators.
    # ===================================================================================================

    def vertices(self):
        return self._vertex_map.items()

    def __iter__(self):
        return iter(self.vertices())
