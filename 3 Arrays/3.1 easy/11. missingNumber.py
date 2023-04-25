def missingNumber(a, n):
    sum = n*(n+1)/2

    arraySum = 0
    for each in a:
        arraySum += each

    return int(sum - arraySum)


print(missingNumber([1, 2, 4, 5], 5))
