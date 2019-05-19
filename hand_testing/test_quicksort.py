def i_partition(arr, low, high):
    i = low
    j = i + 1
    while j < high:
        if arr[j] < arr[i]:
            tmp = arr[i + 1]
            arr[i + 1] = arr[i]
            if j == i + 1:
                arr[i] = tmp
            else:
                arr[i] = arr[j]
                arr[j] = tmp
            i += 1
        j += 1
    return i

def i_quicksort(arr, low, high):
    print(f"Quick Sorting: {arr}, {low} - {high}")
    delta = high-low
    if delta <= 0:
        return
    
    p = i_partition(arr, low, high)
    i_quicksort(arr, low, p)
    i_quicksort(arr, p+1, high)

def quicksort(arr):
    return i_quicksort(arr, 0, len(arr))


if __name__ == "__main__":
    arr = [2, 5, 3, 4, 6, 7, 1, 8, 9, 0, -1, 2]
    result = quicksort(arr)
    print(arr)