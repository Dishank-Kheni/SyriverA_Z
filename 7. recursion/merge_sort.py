def merge_sort(arr, low, high):
    if low == high:
        return

    mid = (low + high) // 2

    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)
    # ptr = 0
    # for i in range(low, high):
    #     arr[i] = temp[ptr]
    #     ptr += 1
    # print(arr)


def merge(arr, low, mid, high):
    temp = []
    left, right = low, mid+1
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    # return temp
    for i in range(low, high+1):
        arr[i] = temp[i-low]


a = [3, 1, 2, 4, 1, 5, 2, 6, 4]
print(a)
merge_sort(a, 0, len(a)-1)
print(a)
