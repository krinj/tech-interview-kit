class Node:
    def __init__(self, v=None):
        self.k = None
        self.v = v
        self.next = None

    def __repr__(self):
        # if self.k is None:
        #     return ""
        return f"{self.k}: {self.v}"


    def __str__(self):
        return self.__repr__()


class HashMap:
    def __init__(self):
        self.arr = []
        self.cap =  0
        self.size = 0
        self.resize(4)

    def resize(self, new_size):
        new_arr = []
        for _ in range(new_size):
            new_arr.append(Node())

        for n in self.arr:
            while n.k is not None:
                self.insert(new_arr, n.k, n.v, new_size)
                n = n.next
        self.arr = new_arr
        self.cap = new_size

    def index(self, k, cap):
        i = hash(k)
        i %= cap
        return i

    def insert(self, arr, k, v, cap):
        i = self.index(k, cap)
        n = arr[i]
        while True:
            if n.k is None:
                n.k = k
                n.next = Node()
                break
            elif n.k == k:
                break
            n = n.next
        n.v = v

    def add(self, k, v):
        self.insert(self.arr, k, v, self.cap)
        self.size += 1
        if self.size >= self.cap:
            new_size = int(self.cap * 2)
            self.resize(new_size)

    def get(self, k):
        i = self.index(k, self.cap)
        n = self.arr[i]

        while True:
            if n.k == None:
                raise Exception(f"Key {k} does not exist.")
            elif n.k == k:
                return n.v
            n = n.next

    def describe(self):
        for i, sub in enumerate(self.arr):
            n = sub
            line = []
            while n.k is not None:
                line.append(str(n))
                n = n.next
            line_str = " -> ".join(line)
            print(f"{i}: {line_str}")
    
def main():
    h = HashMap()
    h.add("A", 5)
    h.add("B", 3)
    h.add("C", 8)
    h.add("A", 2)
    h.describe()

    print(h.get("A"))
    print(h.get("B"))
    print(h.get("C"))


if __name__ == "__main__":
    main()