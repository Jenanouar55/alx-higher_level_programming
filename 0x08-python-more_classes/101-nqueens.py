#!/usr/bin/python3
"""defines a nqueens"""

import sys


def init_board(n):
    """Initialize an `n`x`n sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(" ") for i in range(n) for row in board]
    return board

def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return board

def get_solution(board):
    """Return the current state of the board as a list of queen positions."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
    return solution

def xout(board, row, col):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no
    longer be played are X-ed out.
    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out all downward spots
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # X out all upward spots
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all downward-right spots
    for r, c in zip(range(row + 1, len(board)), range(col + 1, len(board))):
        board[r][c] = "x"
    # X out all downward-left spots
    for r, c in zip(range(row + 1, len(board)), range(col - 1, -1, -1)):
        board[r][c] = "x"
    # X out all upward-right spots
    for r, c in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        board[r][c] = "x"
    # X out all upward-left spots
    for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        board[r][c] = "x"


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    Args:
        board (list): The current working chessboard.
        row (int): The current row to check.
        queens (int): The number of queens to place.
        solutions (list): A list of valid solutions.
    Returns:
        Solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)
            return solutions



if __name__ == "__main__":
    if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
