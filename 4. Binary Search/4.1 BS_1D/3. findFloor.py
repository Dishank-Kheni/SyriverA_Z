
def binarySearch(a, start, end, k):
    
    if start >= len(a):
        return [a[end], -1]

    if end < 0:
        return [a[start] if a[start] < k else -1, a[start] if a[start] > k else -1]

    return [a[start] if a[start] < k else a[end], a[start] if a[start] > k else a[end]]

    mid = (start+end)//2

    # if k == a[mid]:
    #     return mid
    if k < a[mid]:
        return binarySearch(a, start, mid-1, k)
    else:
        return binarySearch(a, mid+1, end, k)


def findFloor(arr, x):
    return binarySearch(arr, 0, len(arr)-1, x)


# print(findFloor([1, 2, 8, 10, 11, 12, 19], 0))
print(findFloor([1, 2, 8, 10, 11, 12, 19], 21))
