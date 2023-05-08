def findKRotation(arr):
    low = 0
    high = len(arr)-1

    mid = -1

    i = len(arr)//2 + 1
    while(i != 0):

        mid = (low+high) // 2

        if arr[mid] < arr[high]:
            high = mid
        else:
            low = mid

        i -= 1

    return high


print(findKRotation([5, 1, 2, 3, 4]))

print(findKRotation([1, 2, 3, 4, 5]))
print(findKRotation([2, 3, 4, 5, 1]))

print(findKRotation([5, 6, 7, 8, 1, 2, 3, 4, ]))


# low != high
# low+1 != high
