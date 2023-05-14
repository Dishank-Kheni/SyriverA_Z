def kthSmallestNum(m, n, k):
    def enough(num):
        count = 0

        for val in range(1, m+1):
            a = min((num // val), n)

            if a == 0:
                break

            count += a

        return count >= k

    left, right = 1, m * n

    while left <= right:
        mid = (left+right)//2
        if enough(mid):
            right = mid
        else:
            left = mid + 1
    return left
