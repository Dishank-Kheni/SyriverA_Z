def countSort(A):
    maxEle = max(A)
    # print(maxEle)
    c = []
    for _ in range(maxEle+1):
        c.append(0)

    for i in range(len(A)):
        c[A[i]] = c[A[i]]+1

    j = 0
    for i in range(maxEle+1):
        if c[i] == 0:
            continue
        else:
            for _ in range(c[i]):
                A[j] = i
                j += 1
                c[i] -= 1

    return A


print(countSort([6, 3, 9, 10, 15, 6, 8, 12, 3, 6]))
