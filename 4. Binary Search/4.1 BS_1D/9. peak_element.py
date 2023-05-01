def peakElement(arr):
    start = 0
    end = len(arr) - 1

    while start < end:

        mid = (start + end)//2

        if mid == 0:
            return arr[0] if arr[0] >= arr[1] else arr[1]

        if mid == len(arr) - 1:
            return arr[len(arr)-1] if arr[len(arr)-1] > arr[len(arr)-2] else arr[len(arr)-2]

        if arr[mid] >= arr[mid - 1] and arr[mid] >= arr[mid + 1]:
            return arr[mid]

        if arr[mid] < arr[mid - 1]:
            end = mid - 1
        else:
            start = mid + 1

    return arr[start]


print(peakElement([4, 3, 2, 1, 8, 9, 7, ]))
