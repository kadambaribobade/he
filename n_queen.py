def print_board(board, n):
    for row in board:
        print(" ".join(row))
    print()


def is_safe(board, row, col, n):

    # Check upper column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n):

    # Base condition
    if row == n:
        print_board(board, n)
        return

    # Try each column
    for col in range(n):

        if is_safe(board, row, col, n):

            # Place queen
            board[row][col] = 'Q'

            # Recursive call
            solve(board, row + 1, n)

            # Backtrack
            board[row][col] = '.'


n = 4

board = [['.' for _ in range(n)] for _ in range(n)]

solve(board, 0, n)