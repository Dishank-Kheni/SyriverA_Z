

def twoSum(a, target):
    c = []

    for i in range(len(a)):
        TGT = target - a[i]
        try:
            index = a.index(TGT)
            return [i, index]
        except:
            pass

    return [-1, -1]


print(twoSum([2, 6, 5, 8, 11], 8))


def twoSumPointer(a, target):
    a.sort()
    i = 0
    j = len(a)-1

    while i < j:
        SUM = a[i]+a[j]
        if SUM < target:
            i += 1
        elif SUM > target:
            j -= 1
        else:
            return True
    print(a)
    return [-1, -1]


print(twoSumPointer([2, 6, 5, 8, 11], 8))
