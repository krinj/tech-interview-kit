from collections import deque

class Node:
    def __init__(self, k=None):
        self.k = k
        self.terminal = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word: str) -> None:
        n = len(word)
        node = self.root

        for i in range(n):
            k = word[i]
            if k not in node.children:
                node.children[k] = Node(k)
            node = node.children[k]

        if node != self.root:
            node.terminal = True

    def validate(self, word: str) -> bool:
        node = self.find_node(word)
        return node is not None and node.terminal

    def find_node(self, word: str):
        n = len(word)
        node = self.root
        for i in range(n):
            k = word[i]
            if k not in node.children:
                return None
            node = node.children[k]
        return node

    def autocomplete(self, prefix: str):
        node = self.find_node(prefix)
        if node is None:
            return []
        return self.bfs(prefix, node)
        
    def bfs(self, prefix, node):
        result = []

        q = deque()
        q.append((prefix, node))

        while len(q) > 0:
            p, n = q.popleft()
            if n.terminal:
                result.append(p)

            for k, n2 in n.children.items():
                p2 = p + k
                q.append((p2, n2))

        return result


def main():
    trie = Trie()
    with open("words.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            word = line.strip().replace("\n", "")
            trie.add(word)
    
    p = "ho"
    result = trie.autocomplete(p)
    print(f"Autocomplete: {p}") 
    print(result)

    w = "hour"
    result = trie.validate(w)
    print(f"Validate {w}: {result}") 

if __name__ == "__main__":
    main()