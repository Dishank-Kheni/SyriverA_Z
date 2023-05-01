def merge_sorted_arrays(a1, a2, m, n):

    j = 0
    for i in range(m-n, m):
        a1[i] = a2[j]
        j += 1

    i = 0
    j = m-n
    k = 0
    for k in range(m-1):
        if a1[i] <= a1[j]:
            a1[k] = a1[i]
            i += 1
        elif a1[i] > a1[j]:
            # a = []
            a1.insert(k, a1.pop(j))
            i += 1
            j += 1

    return a1


print(merge_sorted_arrays([1, 4, 8, 10, 0, 0, 0], [2, 3, 9], 7, 3))
print(merge_sorted_arrays([1], [], 1, 0))
print(merge_sorted_arrays([0], [1], 0, 1))
