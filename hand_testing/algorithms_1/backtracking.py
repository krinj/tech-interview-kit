# N-Queens Problem.
# How many ways can we put N queens on an NxN board?


class Queen:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def safe(q1, q2):
    if q1.x == q2.x:
        return False
    if q1.y == q2.y:
        return False
    if abs(q1.x - q2.x) == abs(q1.y - q2.y):
        return False
    return True


def place(board, n, x):
    if x == n:
        return 1

    count = 0
    for y in range(n):

        q = Queen(x, y)
        valid = True

        for q2 in board:
            if not safe(q, q2):
                valid = False
                break
        
        if valid:
            board.append(q)
            count += place(board, n, x + 1)
            board.pop()

    return count


def main():
    result = place([], 8, 0)
    print(f"Result: {result}")
    pass


if __name__ == "__main__":
    main()