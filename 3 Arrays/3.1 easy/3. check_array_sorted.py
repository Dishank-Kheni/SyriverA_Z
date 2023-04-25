def checkArrraySorted(a):
    sorted = True
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False

    return sorted


print(checkArrraySorted([1, 2, 4, 3, 5]))
