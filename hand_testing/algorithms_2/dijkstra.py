# A ── B ── C
# │    │    
# E ── D ── F
# │         │
# G ── H ── I  

import sys
import heapq

def dijkstra(graph, origin, target):

    dist = {k: [sys.maxsize, None] for k in graph}
    heap = [(0, origin)]
    dist[origin][0] = 0
    print(dist)

    ops = 0

    while True:
        
        print(heap)
        ops += 1
        if len(heap) <= 0:
            for k, v in dist.items():
                print(f"{k}: {v[0]}")

            path = []
            prev = target
            cost = dist[prev][0]
            while prev != origin:
                path.append(prev)
                prev = dist[prev][1]
            path.append(prev)
            path.reverse()
            print(f"Total Ops: {ops}")
            return path, cost

        node = heapq.heappop(heap)[1]
        next = graph[node]
        for n, w in next.items():
            d = w + dist[node][0]
            if d < dist[n][0]:
                dist[n][0] = d
                dist[n][1] = node
                heapq.heappush(heap, (d, n))

    return [], -1


def make_graph():
    graph = {
        "A": {"B": 3, "E": 2},
        "B": {"C": 1, "D": 1, "A": 1},
        "C": {"B": 1},
        "D": {"B": 1, "E": 1, "F": 1},
        "E": {"A": 1, "D": 5, "G": 1},
        "F": {"D": 1, "I": 1},
        "G": {"E": 1, "H": 1},
        "H": {"G": 1, "I": 3},
        "I": {"H": 1}
    }
    return graph


def main():
    graph = make_graph()
    origin = "I"
    target = "A"
    path, cost = dijkstra(graph, origin, target)
    print(f"Path from {origin} to {target}: {path} | Cost: {cost}")


if __name__ == "__main__":
    main()