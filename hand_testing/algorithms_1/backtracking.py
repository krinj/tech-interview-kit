# N-Queens Problem.
# How many ways can we put N queens on an NxN board?


class Queen:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def safe(q1, q2):
    if q1.y == q2.y or q1.x == q2.x:
        return False

    dx = abs(q1.x - q2.x)
    dy = abs(q1.y - q2.y)
    return dx != dy


def place(board, n, x):
    if x == 0:
        return 1

    count = 0
    for y in range(n):
        q = Queen(x, y)
        all_safe = True

        for q2 in board:
            if not safe(q, q2):
                all_safe = False
                break
        
        if not all_safe:
            continue

        board.append(q)
        count += place(board, n, x - 1)
        board.pop()

    return count


def main():
    n = 8
    result = place([], n, n)
    print(f"Result: {result}")
    pass


if __name__ == "__main__":
    main()