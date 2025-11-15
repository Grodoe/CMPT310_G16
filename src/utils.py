# src/utils.py
from src.rules import is_valid_move
from src.board import BLACK, WHITE

def get_valid_moves(board, player):
    moves = []
    for r in range(8):
        for c in range(8):
            if is_valid_move(board, r, c, player):
                moves.append((r, c))
    return moves

def count_discs(board):
    black = (board == BLACK).sum()
    white = (board == WHITE).sum()
    return black, white

def game_over(board):
    return len(get_valid_moves(board, BLACK)) == 0 and len(get_valid_moves(board, WHITE)) == 0
