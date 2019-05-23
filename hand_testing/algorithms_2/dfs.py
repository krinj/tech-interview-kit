# A 🡪 B 🡪 C
# 🡫   🡫    
# E 🡪 D 🡪 F
# 🡫        🡫
# G 🡪 H 🡪 I 🡪 A... 


from collections import deque


def dfs(graph, node, target) -> bool:
    """ Perform Depth First Search on the graph. Return bool (if element is there). """
    seen = set()
    stack = []

    stack.append(node)
    seen.add(node)

    while len(stack) > 0:
        n = stack.pop()
        print(f"Searching: {n}")
        if n == target:
            return True

        for m in graph[n]:
            if m not in seen:
                seen.add(m)
                stack.append(m)

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
    target = "X"

    result = dfs(graph, root_key, target)
    print(f"Path from {root_key} to {target}: {result}")


if __name__ == "__main__":
    main()
