def sortArray(a):
    zero = []
    one = []
    two = []

    for each in a:
        if each == 0:
            zero.append(0)
        elif each == 1:
            one.append(1)
        else:
            two.append(2)

    return zero+one+two


print(sortArray([0, 2, 1, 2, 0, 1]))
