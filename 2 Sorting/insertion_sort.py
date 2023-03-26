def insertion_sort(a):
    for i in range(1, len(a)):
        j = i-1
        x = a[i]

        while j > -1 and a[j] > x:
            a[j+1] = a[j]
            j -= 1
    
        a[j+1] = x
    return a


a = [8, 5, 7, 3, 2]
print(insertion_sort(a))
