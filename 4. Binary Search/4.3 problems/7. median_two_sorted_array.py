def median(num1, num2):
    count = 0
    m = len(num1)
    n = len(num2)
    i = j = 0
    length = (m + n)
    count = 0

    while count < (length)//2:
        if num1[i] < num2[j]:
            count += 1
            i += 1
        else:
            j += 1
            count += 1

    if (length % 2) == 0:
        # print(num1[i-1], num2[j-1])
        return (num1[i-1] + num2[j-1])/2
    else:
        # print(min(num1[i], num2[j]))
        return min(num1[i], num2[j])


print(median([1, 3], [2]))
print(median([1, 3], [2, 4]))
print(median([1], [2]))
print(median([1, 4, 7, 10, 12], [2, 3, 6, 15]))
