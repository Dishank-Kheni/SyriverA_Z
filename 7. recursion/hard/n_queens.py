
def isSafe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def nQueenHelper(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1
            if nQueenHelper(board, col + 1, n):
                return True
            board[i][col] = 0

    return False


def nQueenSolve(n):
    board = [[0 for i in range(n)] for j in range(n)]
    if nQueenHelper(board, 0, n):
        return board
    else:
        return []


if __name__ == "__main__":
    print(nQueenSolve(4))
