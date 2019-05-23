# A ── B ── C
# │    │    
# E ── D ── F
# │         │
# G ── H ── I  

import sys
import heapq

def dijkstra(graph, start, end):

    path = {k: (sys.maxsize, None) for k in graph}

    path[start] = (0, None)
    q = [(0, start)]

    while len(q) > 0:
        print(q)
        cost, node = heapq.heappop(q)
        if node == end:
            result = []
            while node != start:
                result.append(node)
                node = path[node][1]
            result.append(node)
            result.reverse()
            return result, cost

        for m_key, v in graph[node].items():
            m_cost = cost + v
            if m_cost < path[m_key][0]:
                path[m_key] = (m_cost, node)
                heapq.heappush(q, (m_cost, m_key))

    return [], -1


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
    target = "X"
    path, cost = dijkstra(graph, origin, target)
    print(f"Path from {origin} to {target}: {path} | Cost: {cost}")


if __name__ == "__main__":
    main()