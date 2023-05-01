def rowWithMax1s(arr, n, m):

    count = 0
    row = -1
    for i in range(n):
        tempCount = 0

        for j in range(m):
            if arr[i][j] == 1:
                tempCount += 1

        if tempCount > count:
            count = tempCount
            row = i

    return row


print(rowWithMax1s([[0, 1, 1, 1], [0, 0, 1, 1],
      [1, 1, 1, 1], [0, 0, 0, 0]], 4, 4))
