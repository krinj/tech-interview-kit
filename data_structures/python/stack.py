class StackNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self._tail = None
        self._size = 0

    def push(self, x):
        node = StackNode(x)
        if self._tail is not None:
            node.next = self._tail

        self._tail = node
        self._size += 1

    def pop(self):
        if self._tail is not None:
            val = self._tail.val
            self._tail = self._tail.next
            self._size -= 1
            return val
        else:
            return None

    def peek(self):
        if self._tail is not None:
            return self._tail.val
        else:
            return None
    
    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self._size
