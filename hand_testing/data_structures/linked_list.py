class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, x):
        node = Node(x)
        
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    
    def pop(self):
        if self.head is None:
            raise Exception("Cannot pop anymore")
        
        x = self.head.val
        self.head = self.head.next
        if self.head is None:
            self.tail = None

        print(f"Popping: {x}")
        return x

    def traverse(self):
        node = self.head
        s = []
        while node is not None:
            s.append(node.val)
            node = node.next
        
        print(" -> ".join(map(str, s)))

if __name__ == "__main__":
    linked = LinkedList()

    linked.add(6)
    linked.add(7)
    linked.add(8)
    linked.add(2)
    linked.add(15)

    linked.pop()
    linked.pop()
    linked.pop()

    linked.add(1)
    linked.add(3)

    linked.traverse()
