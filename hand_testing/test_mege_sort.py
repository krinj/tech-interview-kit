def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    m = len(arr) // 2
    left = merge_sort(arr[:m])
    right = merge_sort(arr[m:])
    return merge(left, right)


def merge(left, right):
    i = 0
    j = 0
    result =[]
    print("Merging", left, right)
    while True:
        v_left = None if i >= len(left) else left[i]
        v_right = None if j >= len(right) else right[j]

        if v_left is None and v_right is None:
            break

        if v_right is None or (v_left is not None and v_left <= v_right):
            result.append(v_left)
            i += 1
        else:
            result.append(v_right)
            j += 1

    return result


if __name__ == "__main__":
    arr = [2, 5, 3, 4, 6, 7, 1, 8, 9, 0, -1, 2]
    result = merge_sort(arr)
    print(result)