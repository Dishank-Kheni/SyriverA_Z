def triangal(n):
    tr = [[1]*(c+1) for c in range(n)]
    for i in range(n):
        for j in range(1, i):
            # if j == 0 and j == i:
            #     tr[i].append(1)
            #     break

            # if j == 0 or j == i:
            #     tr[i].append(1)
            #     continue

            tr[i][j] = tr[i-1][j] + tr[i-1][j-1]

    return tr


print(triangal(8))
