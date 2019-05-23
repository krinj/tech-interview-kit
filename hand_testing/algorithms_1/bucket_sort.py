# Problem: Print the k most frequent numbers in a list.

def k_most_frequent(arr, k):

    f_map = {}

    for x in arr:
        if x in f_map:
            f_map[x] += 1
        else:
            f_map[x] = 1
    
    buckets = [[] for _ in range(len(arr))]
    for x, count in f_map.items():
        buckets[count].append(x)

    result = []
    for i in range(len(buckets) -1, -1, -1):
        bucket = buckets[i]
        for x in bucket:
            result.append(x)
        if len(result) >= k:
            break
    return result

def main():
    arr = [1, 1, 2, 2, 3, 2, 5, 4, 6, 2, 7, 5, 5, 5, 5, 9, 8, 10]
    print(k_most_frequent(arr, k=2))

if __name__ == "__main__":
    main()