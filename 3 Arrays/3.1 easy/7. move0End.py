def zeroesToEnd(a):
    for i in range(len(a)):
        if a[i] == 0:
            a.append(a.pop(i))
    return a


print(zeroesToEnd([1, 0, 2, 3, 0, 4, 0, 1]))
