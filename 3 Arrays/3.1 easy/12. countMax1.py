def findMaxConsecutiveOnes(a):
    max = count = 0

    for each in a:
        if each == 1:
            count += 1
        else:
            if count > max:
                max = count
            count = 0
    return count if count>max else max


print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
