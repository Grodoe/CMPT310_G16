# src/BasicGreedy.py
import numpy as np

try:
    from src.utils import get_valid_moves
    from src.rules import get_flips
except ModuleNotFoundError:
    from utils import get_valid_moves  
    from rules import get_flips        


class BasicGreedy:
 #Basic greedy AI, only cares about maximizing immediate flips
 
    def select_move(self, board: np.ndarray, player: int):
        moves = get_valid_moves(board, player)
        if not moves:
            return None

        best_move = None
        best_flips = -1
        for (r, c) in moves:
            flips = get_flips(board, r, c, player)
            n_flips = len(flips)
            if n_flips > best_flips:
                best_flips = n_flips
                best_move = (r, c)
        return best_move
