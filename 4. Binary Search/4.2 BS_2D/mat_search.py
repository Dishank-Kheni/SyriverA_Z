from cmath import sqrt


def matSearch(mat, x):
    n = len(mat)
    m = len(mat[0])

    for i in range(n):
        low = 0
        high = m - 1
        mid = -1
        while low <= high:
            mid = (low + high) // 2

            if mat[i][mid] == x:
                return 1
            elif mat[i][mid] > x:
                high = mid-1
            else:
                low = mid+1

    return 0


print(matSearch([[3, 30, 38], [44, 52, 54], [57, 60, 69]], 62))
print(matSearch([[3, 30, 38], [44, 52, 54], [57, 60, 69]], 60))

sqrt(5)
