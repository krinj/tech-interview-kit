# A 🡪 B 🡪 C
# 🡫   🡫    
# E 🡪 D 🡪 F
# 🡫        🡫
# G 🡪 H 🡪 I 🡪 A 


from collections import deque


def bfs(graph, node, e) -> bool:
    """ Perform Breadth First Search on the graph. Return bool (if element is there). """

    seen = set()
    queue = deque()
    queue.append(node)

    while len(queue) > 0:
        n = queue.popleft()
        if n is None or n in seen:
            continue

        if n == e:
            return True

        seen.add(n)
        neighbors = graph[n]
        for next_n in neighbors:
            queue.append(next_n)
    
    return False

def generate_graph():
    graph = {
        "A": ["B", "E"],
        "B": ["C", "D"],
        "C": [],
        "D": ["F"],
        "E": ["D", "G"],
        "F": ["I"],
        "G": ["H"],
        "H": ["I"],
        "I": ["A"]
    }
    return graph


def main():
    graph = generate_graph()

    root_key = "A"
    target = "I"

    result = bfs(graph, root_key, target)
    print(f"Path from {root_key} to {target}: {result}")


if __name__ == "__main__":
    main()
