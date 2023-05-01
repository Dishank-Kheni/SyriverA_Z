def arraySortedOrNot(arr):

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return 0

    return 1


print(arraySortedOrNot([90, 80, 100, 70, 40, 30]))
print(arraySortedOrNot([10, 20, 30, 40, 50]))
