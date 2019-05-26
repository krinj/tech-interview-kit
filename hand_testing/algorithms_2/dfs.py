# A 🡪 B 🡪 C
# 🡫   🡫    
# E 🡪 D 🡪 F
# 🡫        🡫
# G 🡪 H 🡪 I 🡪 A... 


from collections import deque


def dfs(graph, node, x) -> bool:
    """ Perform Depth First Search on the graph. Return bool (if element is there). """
    seen = set()
    stack = [node]

    while len(stack) > 0:
        n = stack.pop()
        if n == x:
            return True
        for child in graph[n]:
            if child not in seen:
                seen.add(child)
                stack.append(child)
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

    root_key = "E"
    target = "B"

    result = dfs(graph, root_key, target)
    print(f"Path from {root_key} to {target}: {result}")


if __name__ == "__main__":
    main()
