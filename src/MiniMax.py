# src/MiniMax.py
import numpy as np
import math
import copy

try:
    from src.utils import get_valid_moves
    from src.rules import get_flips
except ModuleNotFoundError:
    from utils import get_valid_moves
    from rules import get_flips


class MinimaxAI:
    def __init__(self, depth=3,player=1):
        self.depth = depth
        self.player = player

    def select_move(self, board, player):
        moves = get_valid_moves(board, player)
        if not moves:
            return None

        best_score = -math.inf
        best_move = None

        for move in moves:
            new_board = board.copy()
            self.apply_move(new_board, move, player)
            score = self.minimax(new_board, self.depth - 1, -player,
                                  alpha=-math.inf, beta=math.inf)
            if score > best_score:
                best_score = score
                best_move = move

        return best_move


    def minimax(self, board, depth, player, alpha, beta):
        if depth == 0:
            return self._evaluate(board) 

        moves = get_valid_moves(board, player)
        if not moves:
            # pass turn
            return self.minimax(board, depth - 1, -player, alpha, beta)

        if player == self.player:  # maximize
            max_eval = -math.inf
            for move in moves:
                new_board = board.copy()
                self.apply_move(new_board, move, player)
                eval = self.minimax(new_board, depth - 1, -player, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:  # minimize
            min_eval = math.inf
            for move in moves:
                new_board = board.copy()
                self.apply_move(new_board, move, player)
                eval = self.minimax(new_board, depth - 1, -player, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def _evaluate(self, board):
        # Disc difference
        my_discs = np.sum(board == self.player)
        opp_discs = np.sum(board == -self.player)
        disc_score = my_discs - opp_discs

        # Mobility
        my_moves = len(get_valid_moves(board, self.player))
        opp_moves = len(get_valid_moves(board, -self.player))
        mobility_score = my_moves - opp_moves

        # Corners
        corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
        my_corners = sum(1 for r, c in corners if board[r, c] == self.player)
        opp_corners = sum(1 for r, c in corners if board[r, c] == -self.player)
        corner_score = 25 * (my_corners - opp_corners)

        return 10 * disc_score + 5 * mobility_score + corner_score

 
    def apply_move(self, board, move, player):
        r, c = move
        flips = get_flips(board, r, c, player)
        board[r, c] = player
        for fr, fc in flips:
            board[fr, fc] = player
