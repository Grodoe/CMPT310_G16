# src/BasicRandom.py
import numpy as np

try:
    from src.utils import get_valid_moves
except ModuleNotFoundError:
    from utils import get_valid_moves


class BasicRandom:
    # Random AI: picks a random valid move, ignores board position / flips
    def __init__(self, player=1):
        self.player = player

    def select_move(self, board: np.ndarray, player: int):
        moves = get_valid_moves(board, player)
        if not moves:
            return None

        # Pick a random move from the list of valid moves
        idx = np.random.randint(len(moves))
        return moves[idx]
