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
        n = self.root
        for c in word:
            if c not in n.children:
                n.children[c] = Node()
            n = n.children[c]
        n.terminal = True

    def validate(self, word: str) -> bool:
        n = self.find_node(word)
        if n is None or not n.terminal:
            return False
        return True

    def find_node(self, word: str):
        n = self.root
        for c in word:
            if c not in n.children:
                return None
            n = n.children[c]
        return n

    def autocomplete(self, prefix: str):
        n = self.find_node(prefix)
        result = []
        self.dfs(result, prefix, n)
        return result
        
    def dfs(self, arr, p, n):
        if n is None:
            return
        if n.terminal:
            arr.append(p)
        for k, c in n.children.items():
            self.dfs(arr, p + k, c)


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