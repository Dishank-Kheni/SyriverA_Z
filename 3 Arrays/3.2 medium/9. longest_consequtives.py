def longestConsequtives(a):
    a.sort()
    count = max = 1

    for i in range(len(a)-1):
        if a[i+1] == a[i]+1:
            count += 1
        else:
            if count > max:
                max = count
            count = 1
    if count > max:
        max = count
    return max


print(longestConsequtives([100, 200, 1, 3, 2, 4]))
print(longestConsequtives([3, 8, 5, 7, 6]))
