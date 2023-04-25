from copy import copy, deepcopy


def setMatrixZero(a):
    row = len(a)
    column = len(a[0])

    # c = [[1][1][1]]
    matrix = deepcopy(a)

    for i in range(row):
        for j in range(column):
            if a[i][j] == 0:
                for m in range(j, -1, -1):
                    matrix[i][m] = 0

                for m in range(j, column, 1):
                    matrix[i][m] = 0

                for m in range(i, -1, -1):
                    matrix[m][j] = 0

                for m in range(i, row, 1):
                    matrix[m][j] = 0

    return matrix


print(setMatrixZero([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
