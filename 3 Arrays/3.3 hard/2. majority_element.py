def majorityElement(a, n):
    result = []
    a.sort()
    i = 0

    mapp = {}

    for i in range(len(a)):
        count = mapp.get(a[i], 0)
        count += 1
        mapp[a[i]] = count
        if count > n//3:
            result.append(a[i])

    return result


print(majorityElement([1, 2, 2, 3, 2], 5))
