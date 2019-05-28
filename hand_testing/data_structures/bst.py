from vis_tree import visualize_tree
from vis_tree import Node


def create_bst(arr, low, high):
    delta = high - low
    if delta == 0:
        return None

    m = low + delta // 2
    n = Node(arr[m])
    n.left = create_bst(arr, low, m)
    n.right = create_bst(arr, m + 1, high)
    return n


def main():
    arr = list(range(9))
    node = create_bst(arr, 0, len(arr))
    visualize_tree(node)

if __name__ == "__main__":
    main()