class Node:
    def __init__(self, x):
        self.next: 'Node' = None
        self.prev: 'Node' = None
        self.x = x


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size: int = 0

    # ===================================================================================================
    # Add an element x (can be any type) to the head or tail.
    # ===================================================================================================

    def add_head(self, x):
        node = Node(x)
        if self.size() == 0:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self._size += 1

    def add_tail(self, x):
        node = Node(x)
        if self.size() == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self._size += 1

    # ===================================================================================================
    # Pop an element from the head or tail, and return it.
    # ===================================================================================================

    def pop_head(self):
        x, result = self._final_removal()
        if result:
            return x
        else:
            x = self.head.x
            next_node = self.head.next
            next_node.prev = None
            self.head.next = None
            self.head = next_node
            return x

    def pop_tail(self):
        x, result = self._final_removal()
        if result:
            return x
        else:
            x = self.tail.x
            prev_node = self.tail.prev
            prev_node.next = None
            self.tail.prev = None
            self.tail = prev_node
            return x

    def _final_removal(self):
        if self.size() == 0:
            return None, True
        self._size -= 1
        if self.size() == 0:
            x = self.head.x
            self.head = None
            self.tail = None
            return x, True
        else:
            return None, False

    # ===================================================================================================
    # Return the head or tail element without removing it.
    # ===================================================================================================

    def peek_head(self):
        if self.head is not None:
            return self.head.x
        else:
            return None

    def peek_tail(self):
        if self.tail is not None:
            return self.tail.x
        else:
            return None

    # ===================================================================================================
    # Return the size of the list.
    # ===================================================================================================

    def size(self) -> int:
        return self._size

    # ===================================================================================================
    # Optional Utility Functions
    # ===================================================================================================

    def __repr__(self):
        elements = []
        node = self.head
        while node is not None:
            elements.append(node.x)
            node = node.next
        content = " -> ".join(map(str, elements))
        return f"[{content}]"

    def display(self):
        print(self)
