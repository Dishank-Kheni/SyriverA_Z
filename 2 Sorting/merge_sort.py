def merge(a, b):
    i = j = 0
    c = []
    while(i < len(a) and j < len(b)):

        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    for i in range(i, len(a)):
        c.append(a[i])

    for j in range(j, len(b)):
        c.append(b[j])

    return c


a = [1, 5, 8, 14, 18]
b = [2, 5, 6, 23]

print(merge(a, b))
