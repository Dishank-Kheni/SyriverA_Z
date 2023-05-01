def binarySearch(a, start, end, k):
    if start > end:
        return -1

    mid = (start+end)//2

    if k == a[mid]:
        return mid
    elif k < a[mid]:
        return binarySearch(a, start, mid-1, k)
    else:
        return binarySearch(a, mid+1, end, k)


print(binarySearch([2, 3, 7, 10, 13, 14, 17], 0, 6, 14))
