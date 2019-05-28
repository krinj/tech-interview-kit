def i_partition(arr, low, high):
    i = low
    j = i + 1
    while j < high:
        if arr[j] < arr[i]:
            tmp = arr[i]
            arr[i] = arr[j]
            if j == i + 1:
                arr[j] = tmp
            else:
                arr[j] = arr[i + 1]
                arr[i + 1] = tmp
                i += 1
        j += 1
    return i

def i_quicksort(arr, low, high):
    if high - low <= 1:
        return
    
    p = i_partition(arr, low, high)
    i_quicksort(arr, low, p)
    i_quicksort(arr, p + 1, high)

def quicksort(arr):
    return i_quicksort(arr, 0, len(arr))


if __name__ == "__main__":
    arr = [2, 5, 3, 4, 6, 7, 1, 8, 9, 0, -1, 2]
    result = quicksort(arr)
    print(arr)