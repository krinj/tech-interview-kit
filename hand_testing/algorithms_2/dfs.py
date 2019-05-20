# A 🡪 B 🡪 C
# 🡫   🡫    
# E 🡪 D 🡪 F
# 🡫        🡫
# G 🡪 H 🡪 I 🡪 A... 


from collections import deque


def dfs(graph, node, e, visited) -> bool:
    """ Perform Depth First Search on the graph. Return bool (if element is there). """

    if node == e:
        return True

    if node in visited:
        return False

    visited.add(node)

    for n in graph[node]:
        if dfs(graph, n, e, visited):
            return True

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
    target = "A"

    result = dfs(graph, root_key, target, set())
    print(f"Path from {root_key} to {target}: {result}")


if __name__ == "__main__":
    main()
