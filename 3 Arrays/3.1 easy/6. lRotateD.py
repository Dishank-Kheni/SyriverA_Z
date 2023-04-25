def leftRotate(a, d):
    while d != 0:
        val = a.pop(0)
        a.append(val)
        d -= 1

    return a


print(leftRotate([1, 2, 3, 4, 5, 6, 7], 3))
# print(leftRotate([1]))
