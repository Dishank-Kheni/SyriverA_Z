def getElements(a):
    a.sort()
    return (a[1], a[-2])


print(getElements([8, 5, 7, 3, 2]))


def getElements1(a):
    for i in range(2):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    i = 0
    k = 0
    for i in range(2):

        j = i
        k = i
        for j in range(i, len(a)):
            if a[j] < a[k]:
                k = j

        a[i], a[k] = a[k], a[i]

    return (a[1], a[-2])


print(getElements1([8, 5, 7, 3, 2]))
