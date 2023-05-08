def floorSqrt(x):
    if x == 0 or x == 1:
        return x

    left, right = 1, x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1

    return ans


print(floorSqrt(5))
print(floorSqrt(4))
