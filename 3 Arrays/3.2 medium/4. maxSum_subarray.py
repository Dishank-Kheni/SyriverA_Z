import sys

# INSPIRED


def maxSubarraySum(a):
    maxi = -sys.maxsize-1
    sum = 0

    for i in range(len(a)):
        sum += a[i]

        if sum > maxi:
            maxi = sum

        if sum < 0:
            sum = 0

    return maxi


print(maxSubarraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
