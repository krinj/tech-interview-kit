# A 🡪 B 🡪 C
# 🡫   🡫    
# E 🡪 D 🡪 F
# 🡫        🡫
# G 🡪 H 🡪 I  


def top_sort(graph):

    n_inbound = {}
    for k, nodes in graph.items():
        for n in nodes:
            if n not in n_inbound:
                n_inbound[n] = 1
            else:
                n_inbound[n] += 1

        if k not in n_inbound:
                n_inbound[k] = 0

    stack = [n for n, v in n_inbound.items() if v == 0]
    result = []

    while len(stack) > 0:
        n = stack.pop()
        result.append(n)

        for k in graph[n]:
            n_inbound[k] -= 1
            if n_inbound[k] == 0:
                stack.append(k)
                
    if len(result) == len(graph):
        return result
    else:
        return None


def make_graph():
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
    graph = make_graph()
    result = top_sort(graph)
    print(f"Topological Sort: {result}")


if __name__ == "__main__":
    main()