# src/nn_agent.py
import numpy as np
import torch
from src.nn_utils import encode_board
from src.rules import apply_move
from src.utils import get_valid_moves

class NeuralNetAgent:
    def __init__(self, model, player, device="cpu"):
        self.model = model
        self.player = player
        self.device = device

    def choose_move(self, board):
        valid_moves = get_valid_moves(board, self.player)
        if not valid_moves:
            return None

        best_move = None
        best_value = -999.0

        for (r, c) in valid_moves:
            new_board = board.copy().astype(int)
            apply_move(new_board, r, c, self.player)

            inp = encode_board(new_board, self.player).to(self.device)
            with torch.no_grad():
                value = self.model(inp).item()

            if value > best_value:
                best_value = value
                best_move = (r, c)

        return best_move
