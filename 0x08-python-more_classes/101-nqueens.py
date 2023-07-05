#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    # Check if it's safe to place a queen at board[row][col]

    # Check the row
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check the upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True

def solve_nqueens(board, col):
    # Recursive function to solve the N-queens problem

    if col == N:
        # All queens are placed, print the solution
        print_solution(board)
        return

    for i in range(N):
        if is_safe(board, i, col):
            # Place a queen at board[i][col]
            board[i][col] = 'Q'

            # Recur to place the rest of the queens
            solve_nqueens(board, col + 1)

            # Backtrack and remove the queen from board[i][col]
            board[i][col] = '.'

def print_solution(board):
    # Print the board configuration

    for row in board:
        print(' '.join(row))
    print()

# Main program

# Check the command-line arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Create an empty chessboard
board = [['.' for _ in range(N)] for _ in range(N)]

# Solve the N-queens problem
solve_nqueens(board, 0)
