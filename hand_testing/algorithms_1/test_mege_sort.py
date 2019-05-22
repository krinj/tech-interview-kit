def merge_sort(arr, low, high):
    
    delta = high - low
    if delta <= 1:
        return arr[low:high]
    
    m = low + delta // 2
    left = merge_sort(arr, low, m)
    right = merge_sort(arr, m, high)
    result = merge(left, right)
    return result


def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) or j < len(right):

        vi = None if i >= len(left) else left[i]
        vj = None if j >= len(right) else right[j]

        if vj is None or (vi is not None and vi <= vj):
            result.append(vi)
            i += 1
        else:
            result.append(vj)
            j += 1

    return result


if __name__ == "__main__":
    arr = [2, 5, 3, 4, 6, 7, 1, 8, 9, 0, -1, 2, 5]
    result = merge_sort(arr, 0, len(arr))
    print(result)