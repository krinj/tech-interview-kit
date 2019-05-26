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
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node(c)
            node = node.children[c]
        node.terminal = True

    def validate(self, word: str) -> bool:
        node = self.find_node(word)
        return node.terminal

    def find_node(self, word: str):
        node = self.root
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def autocomplete(self, prefix: str):
        node = self.find_node(prefix)
        words = []
        self.dfs(words, prefix, node)
        return words
        
    def dfs(self, words, prefix, node):
        if node.terminal:
            words.append(prefix)

        for k, next_node in node.children.items():
            self.dfs(words, prefix + k, next_node)


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