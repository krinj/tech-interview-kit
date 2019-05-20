

def knapsack(items, max_w, memo, i):

    key = (i, max_w)
    if key in memo:
        return memo[key]

    if i < 0:
        return (0, [])

    v1, sack1 = knapsack(items, max_w, memo, i - 1)

    item = items[i]
    if item.weight <= max_w:

        v2, sack2 = knapsack(items, max_w - item.weight, memo, i - 1)
        v2 += item.value

        result = max(v1, v2)
        if v1 == result:
            sack = sack1[:]
        else:
            sack = sack2[:]
            sack.append(item.key)
    else:

        result = v1
        sack = sack1[:]
    
    memo[key] = (result, sack)
    return memo[key]


class Item:
    def __init__(self, k, v=10, w=10):
        self.key = k
        self.value = v
        self.weight = w


def main():
    items = [
        Item("A", 120, 30),
        Item("B", 70, 20),
        Item("C", 500, 5),
        Item("D", 100, 15),
        Item("E", 15, 1),
        Item("F", 200, 80)
    ]
    max_weight = 100
    memo = {}
    result = knapsack(items, max_weight, memo, len(items) - 1)
    print(f"Results: {result}")


if __name__ == "__main__":
    main()