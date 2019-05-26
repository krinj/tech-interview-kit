# A 🡪 B 🡪 C
# 🡫       
# E 🡪 D 🡪 F
# 🡫        🡫
# G 🡪 H 🡪 I  


def top_sort(graph):
    d_map = {k: 0 for k in graph}
    for nodes in graph.values():
        for n in nodes:
            d_map[n] += 1
    
    valid_nodes = [k for k, v in d_map.items() if v == 0]
    result =[]

    while len(valid_nodes) > 0:
        n = valid_nodes.pop()
        result.append(n)
        for c in graph[n]:
            d_map[c] -= 1
            if d_map[c] == 0:
                valid_nodes.append(c)
    
    if len(result) == len(graph):
        return result
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