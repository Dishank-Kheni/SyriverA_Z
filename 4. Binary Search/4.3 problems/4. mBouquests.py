def minDays(bloomDay, m, k):

    def feasible(days):
        flowers = bonquets = 0

        for bloom in bloomDay:
            if bloom > days:
                flowers = 0
            else:
                bonquets += (flowers + 1) // k
                flowers = (flowers + 1) % k
        return bonquets >= m

    if len(bloomDay) < m * k:
        return -1

    left, right = 1, max(bloomDay)

    while left < right:
        mid = (left+right)//2

        if feasible(mid):
            right = mid
        else:
            left = mid + 1

        return left


print(minDays([1, 10, 3, 10, 2], 3, 1))
print(minDays([1, 10, 3, 10, 2], 3, 2))
print(minDays([7, 7, 7, 7, 12, 7, 7], 2, 2))
