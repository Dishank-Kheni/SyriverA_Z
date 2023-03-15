def reverse_aaray(array, n):
    for i in range(0, n//2, 1):
        temp = array[i]
        array[i] = array[n-i-1]
        array[n-i-1] = temp
    return array


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(array)

print(reverse_aaray(array, n))
