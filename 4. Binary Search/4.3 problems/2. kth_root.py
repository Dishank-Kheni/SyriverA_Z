def nThRoot(n, m):
    if m == 0 or m == 1:
        return m

    left, right = 1, m
    while left <= right:
        mid = (left + right) // 2
        if pow(mid, n) == m:
            return mid
        elif pow(mid, n) < m:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1

    return ans


# nThRoot(3, 27)
print(nThRoot(2, 16))
print(nThRoot(5, 243))
