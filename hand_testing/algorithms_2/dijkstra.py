# A ── B ── C
# │    │    
# E ── D ── F
# │         │
# G ── H ── I  

import sys
import heapq

def dijkstra(graph, start, end):

    paths = {k:(sys.maxsize, None) for k in graph}
    paths[start] = (0, None)
    heap = [(0, start)]

    while len(heap) > 0:
        d, k = heapq.heappop(heap)
        if k == end:
            final_path = []
            while k != start:
                final_path.append(k)
                k = paths[k][1]
            final_path.append(k)
            final_path.reverse()
            return d, final_path

        for n in graph[k]:
            dn = d + graph[k][n]
            if dn < paths[n][0]:
                paths[n] = dn, k
                heapq.heappush(heap, (dn, n))
    return -1, []


def make_graph():
    graph = {
        "A": {"B": 3, "E": 2},
        "B": {"C": 1, "D": 1, "A": 1},
        "C": {"B": 1},
        "D": {"B": 1, "E": 1, "F": 1},
        "E": {"A": 1, "D": 5, "G": 1},
        "F": {"D": 1, "I": 1},
        "G": {"E": 10, "H": 1},
        "H": {"G": 1, "I": 3},
        "I": {"H": 1, "F": 2}
    }
    return graph


def main():
    graph = make_graph()
    origin = "I"
    target = "A"
    cost, path = dijkstra(graph, origin, target)
    print(f"Path from {origin} to {target}: {path} | Cost: {cost}")


if __name__ == "__main__":
    main()