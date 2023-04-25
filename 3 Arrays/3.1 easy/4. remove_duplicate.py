def removeDuplicate(a):

    i = 1
    j = len(a)
    while i < j:
        if a[i-1] == a[i]:
            a.pop(i)
            j -= 1
        else:
            i += 1
    return a


print(removeDuplicate([1, 1, 2, 2, 2, 3, 3]))
