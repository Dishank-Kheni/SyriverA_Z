
def binarySearch(a, start, end, k):
    if start > end:
        if start >= len(a):
            return end + 1

        if end < 0:
            return start+1 if a[start] < k else 0

        return start+1 if a[start] < k else end+1

    mid = (start+end)//2

    if k == a[mid]:
        return mid
    if k < a[mid]:
        return binarySearch(a, start, mid-1, k)
    else:
        return binarySearch(a, mid+1, end, k)


def searchInsertK(arr, k):
    return binarySearch(arr, 0, len(arr), k)


print(searchInsertK([1, 3, 5, 6], 5))
print(searchInsertK([1, 3, 5, 6], 2))
