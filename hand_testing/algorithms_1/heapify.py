def heapify(arr, i, end):

    left = 2 * i + 1
    right = left + 1
    print(f"Processing {i}")
    v_left = arr[left] if left < end else None
    v_right = arr[right] if right < end else None

    if v_left is None and v_right is None:
        return
    
    if v_right is None or v_left > v_right:
        v = v_left
        v_idx = left
    else:
        v = v_right
        v_idx = right
    
    print(f"Compare {v} and {arr[i]}")
    if v > arr[i]:
        print(f"Swapping {v} and {arr[i]}")
        arr[v_idx] = arr[i]
        arr[i] = v
        heapify(arr, v_idx, end)

def create_heap(arr):

    i = len(arr) // 2 - 1
    while i >= 0:
        heapify(arr, i, len(arr))
        i -= 1


def heap_sort(arr):

    create_heap(arr)

    j = len(arr) - 1
    while j > 0:
        tmp = arr[j]
        arr[j] = arr[0]
        arr[0] = tmp

        heapify(arr, 0, j)
        j -= 1

def main():
    arr = [1, 8, 5, 3, 4, 2, 9]
    heap_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()