def lineraSearch(a, num):
    for each in a:
        if each == num:
            return True

    return False


print(lineraSearch([1, 2, 3, 4, 5], 4))
