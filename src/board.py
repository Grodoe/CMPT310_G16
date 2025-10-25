# src/board.py
import numpy as np

EMPTY, BLACK, WHITE = 0, 1, -1
BOARD_SIZE = 8

def create_board():
    board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
    # Starting 4 pieces in the center
    board[3, 3] = WHITE
    board[3, 4] = BLACK
    board[4, 3] = BLACK
    board[4, 4] = WHITE
    return board

def print_board(board):
    symbols = {EMPTY: '.', BLACK: 'B', WHITE: 'W'}
    for row in board:
        print(' '.join(symbols[val] for val in row))
    print()


