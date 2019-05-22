def heapify(arr, i, end):
    left = i * 2 + 1
    right = left + 1

    v_left = arr[left] if left < end else None
    v_right = arr[right] if right < end else None

    if v_left is None and v_right is None:
        return

    if v_right is None or (v_left is not None and v_left >= v_right):
        v_max = v_left
        v_idx = left
    else:
        v_max = v_right
        v_idx = right
    
    if v_max > arr[i]:
        arr[v_idx] = arr[i]
        arr[i] = v_max
        heapify(arr, v_idx, end)

def create_heap(arr):
    end = len(arr)
    i = end // 2 - 1

    while i >= 0:
        heapify(arr, i, end)
        i -= 1

def heap_sort(arr):
    create_heap(arr)
    i = len(arr) - 1
    while i > 0:
        tmp = arr[i]
        arr[i] = arr[0]
        arr[0] = tmp

        heapify(arr, 0, i)
        i -= 1

def main():
    arr = [1, 8, 5, 3, 4, 2, 9]
    # create_heap(arr)
    heap_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()