def partition(a, l, h):
    pivot = a[l]
    i, j = l, h
    while(i < j):
        while(a[i] <= pivot):
            i += 1
        while(a[j] > pivot):
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def QuickSort(a, l, h):
    if (l < h):
        j = partition(a, l, h)
        QuickSort(a, l, j)
        QuickSort(a, j+1, j)


A = [11, 13, 7, 12, 16, 9, 24, 5, 10, 3, ]
QuickSort(A, 0, 10)
print(A)
