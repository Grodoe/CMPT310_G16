# src/rules.py
from src.board import EMPTY, BLACK, WHITE, BOARD_SIZE

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1),  (1, 0), (1, 1)]

def is_on_board(r, c):
    return 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE

def get_flips(board, row, col, player):
    if board[row, col] != EMPTY:
        return []
    
    opponent = -player
    flips = []

    for dr, dc in DIRECTIONS:
        r, c = row + dr, col + dc
        tiles_to_flip = []

        while is_on_board(r, c) and board[r, c] == opponent:
            tiles_to_flip.append((r, c))
            r += dr
            c += dc

        if is_on_board(r, c) and board[r, c] == player and tiles_to_flip:
            flips.extend(tiles_to_flip)
    
    return flips

def is_valid_move(board, row, col, player):
    return len(get_flips(board, row, col, player)) > 0

def apply_move(board, row, col, player):
    flips = get_flips(board, row, col, player)
    if not flips:
        return False  # Invalid move
    board[row, col] = player
    for (r, c) in flips:
        board[r, c] = player
    return True
