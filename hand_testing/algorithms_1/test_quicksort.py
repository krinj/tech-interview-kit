def i_partition(arr, low, high):
    i = low
    for j in range(i + 1, high):
        if arr[j] < arr[i]:
            tmp = arr[i]
            if j == i + 1:
                arr[i] = arr[j]
                arr[j] = tmp
            else:
                arr[i] = arr[j]
                arr[j] = arr[i + 1]
                arr[i + 1] = tmp
            i += 1
    return i

def i_quicksort(arr, low, high):
    delta = high - low
    if delta == 0:
        return

    m = i_partition(arr, low, high)
    i_quicksort(arr, low, m)
    i_quicksort(arr, m + 1, high)

def quicksort(arr):
    return i_quicksort(arr, 0, len(arr))


if __name__ == "__main__":
    arr = [2, 5, 3, 4, 6, 7, 1, 8, 9, 0, -1, 2]
    result = quicksort(arr)
    print(arr)