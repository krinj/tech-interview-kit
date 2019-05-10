from typing import List


class HashNode:
    def __init__(self):
        self.key = None
        self.val = None
        self.next: HashNode = None


class HashMap:

    def __init__(self):
        self._storage: List[HashNode] = []
        self._capacity = 0
        self._limit = 0  # When the capacity reaches this, then resize the array.
        self._size = 0
        self.resize(8)

    def resize(self, new_size: int):
        old_capacity = self._capacity

        # Increase the capacity.
        new_storage = []
        for _ in range(new_size):
            new_storage.append(HashNode())

        self._capacity = new_size
        self._limit = int(self._capacity * 0.7)

        # Move the items.
        for i in range(old_capacity):
            node = self._storage[i]
            while node.key is not None:
                self._set_item_to_array(node.key, node.val, new_storage)
                node = node.next

        # Set the storage to the new.
        self._storage = new_storage

    @staticmethod
    def get_hash_index(key, capacity):
        return hash(key) % capacity

    def __getitem__(self, key):
        index = self.get_hash_index(key, len(self._storage))
        node = self._storage[index]
        while node.key != key:
            node = node.next
            if node is None:
                raise Exception(f"Key {key} not found in Hash Table.")
        return node.val

    def __setitem__(self, key, value):

        if key is None:
            raise Exception("Cannot use None for key.")
        size_increase = self._set_item_to_array(key, value, self._storage)

        self._size += size_increase
        if self._size >= self._limit:
            self.resize(int(self._capacity * 1.5))

    def _set_item_to_array(self, key, value, array):
        index = self.get_hash_index(key, len(array))
        node = array[index]

        while node.key is not None and node.key != key:
            node = node.next

        node.key = key
        node.val = value
        if node.next is None:
            node.next = HashNode()
            return 1
        else:
            return 0

    def size(self):
        return self._size

    def display(self):

        for i in range(self._capacity):
            display_line = [f"{str(i).zfill(3)}: ["]
            node = self._storage[i]
            while node.key is not None:
                display_line.append(f"{node.key} ({node.val})")

                if node.next.key is not None:
                    display_line.append(" -> ")

                node = node.next

            display_line.append("]")
            print("".join(display_line))

        print(f"\nCapacity: {self._capacity}")
        print(f"Size: {self._size}")
        print(f"Limit: {self._limit}")
