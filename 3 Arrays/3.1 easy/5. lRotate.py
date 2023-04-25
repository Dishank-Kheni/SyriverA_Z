def leftRotate(a):
    val = a.pop(0)
    a.append(val)

    return a


print(leftRotate([1, 2, 3, 4, 5]))
print(leftRotate([1]))

