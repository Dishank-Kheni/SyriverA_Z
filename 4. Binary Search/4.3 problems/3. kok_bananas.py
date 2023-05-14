import math


def minEatingSpeed(piles, h):
    def feasible(s):
        # return sum(math.ceil(pile / s) for pile in piles) <= h
        # return sum((pile - 1) / s + 1 for pile in piles) <= h
        hrs = 0
        for pile in piles:
            if pile <= s:
                hrs += 1
            else:
                while pile > 0:
                    pile = pile - s
                    hrs += 1

        return True if hrs <= h else False

    left, right = 1, max(piles)

    while left < right:

        mid = (left + right) // 2

        if feasible(mid):
            right = mid
        else:
            left = mid + 1

    return left


print(minEatingSpeed([3, 6, 7, 11], 8))
print(minEatingSpeed([30, 11, 23, 4, 20], 5))
print(minEatingSpeed([30, 11, 23, 4, 20], 6))
