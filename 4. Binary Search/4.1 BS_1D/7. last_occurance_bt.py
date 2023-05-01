def lastOccurance(arr, k):
    start = 0
    end = len(arr) - 1
    mid = loc = -1
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] < k:
            start = mid+1
        elif arr[mid] > k:
            end = mid - 1

        if arr[mid] == k:
            while mid <= len(arr)-1 and arr[mid] == k:
                mid += 1
            loc = mid - 1
            break

    return loc


print(lastOccurance([3, 3, 4, 13, 13, 13, 20, 40], 3))
print(lastOccurance([3, 4, 13, 13, 13, 20, 40], 60))
