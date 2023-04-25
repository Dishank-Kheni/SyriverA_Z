def intersection(a, b):
    i = j = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            c.append(a[i])
            i += 1
            j += 1

    return c


print(intersection([1, 2, 3, 4, 5], [2, 3, 4, 4, 5]))
print(intersection([1, 2, 3, 3, 4, 5, 6, 7], [3, 3, 4, 4, 5, 8]))
