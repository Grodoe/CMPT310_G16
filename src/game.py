# src/game.py
import numpy as np
from src.board import create_board, BLACK, WHITE
from src.utils import get_valid_moves, count_discs, game_over
from src.rules import apply_move

class ReversiGame:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = create_board()
        self.current_player = BLACK

    def step_move(self, row, col):
        if apply_move(self.board, row, col, self.current_player):
            self.current_player *= -1  # switch turns
            return True
        return False

    def available_moves(self):
        return get_valid_moves(self.board, self.current_player)

    def is_over(self):
        return game_over(self.board)

    def score(self):
        return count_discs(self.board)
