# A 🡪 B 🡪 C
# 🡫   🡫    
# E 🡪 D 🡪 F
# 🡫        🡫
# G 🡪 H 🡪 I  


from collections import deque


def bfs(graph, root_key, e) -> bool:
    """ Perform Breadth First Search on the graph. Return bool (if element is there). """

    queue = deque()
    queue.append(root_key)

    while len(queue) > 0:
        node = queue.popleft()
        if node == e:
            return True
        next = graph[node]
        for k in next:
            queue.append(k)

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
        "I": []
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
