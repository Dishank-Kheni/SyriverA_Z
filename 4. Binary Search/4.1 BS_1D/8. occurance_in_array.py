def countOccurance(arr, k):
    start = 0
    end = len(arr) - 1
    mid = -1
    count = 0
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] < k:
            start = mid+1
        elif arr[mid] > k:
            end = mid - 1

        if arr[mid] == k:
            j = mid
            while j <= len(arr)-1 and arr[j] == k:
                j += 1
                count += 1
            j = mid-1
            while j >= 0 and arr[j] == k:
                j -= 1
                count += 1
            break

    return count


print(countOccurance([3, 3, 4, 13, 13, 13, 20, 40], 3))
print(countOccurance([3, 4, 13, 13, 13, 20, 40], 60))
