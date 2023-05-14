from math import ceil


def smallerDivisor(num, threshold):

    def condition(divisor):
        sum_division = sum(ceil(each/divisor) for each in num)
        return sum_division <= threshold

    left, right = 1, max(num)
    while left < right:
        mid = (left+right)//2
        if condition(mid):
            right = mid
        else:
            left = mid+1

    return left


print(smallerDivisor([1, 2, 5, 9], 6))
print(smallerDivisor([44, 22, 33, 11, 1], 5))
