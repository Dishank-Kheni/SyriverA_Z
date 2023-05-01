def find_missing_repeating(a):
    result = []
    a.sort()

    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            result.append(a[i])

        if a[i]-1 != a[i-1]:
            j = a[i] - 1
            while j > a[i-1]:
                result.append(j)
                j -= 1

    return result


print(find_missing_repeating([3, 1, 2, 5, 3]))
print(find_missing_repeating([3, 1, 2, 5, 4, 6, 7, 5]))
