

def bubble_sort(arr):
    for i in range(len(arr)-1):
        flag = 0
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1

        if flag == 0:
            break

    return arr


arr = [3, 7, 9, 10, 6, 5, 12, 4, 11, 2]

print(bubble_sort(arr))
