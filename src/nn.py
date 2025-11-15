# src/nn.py
import torch
import numpy as np
from src.nn_model import ReversiValueNet
from src.rules import get_flips
from src.utils import get_valid_moves

class NeuralNetworkAI:
    def __init__(self, model_path=None):
        self.model = ReversiValueNet()
        self.model.eval()

        if model_path is not None:
            self.model.load_state_dict(torch.load(model_path, map_location="cpu"))
            print("Loaded neural network model:", model_path)

    # Convert board to NN input: shape (1, 1, 8, 8)
    def encode(self, board, player):
        arr = board.astype(np.float32) * player  # flip perspective
        tensor = torch.tensor(arr).unsqueeze(0).unsqueeze(0)  # (1,1,8,8)
        return tensor

    # Simulate a move
    def apply_move(self, board, move, player):
        r, c = move
        flips = get_flips(board, r, c, player)
        new_board = board.copy()
        new_board[r, c] = player
        for fr, fc in flips:
            new_board[fr, fc] = player
        return new_board

    def get_move(self, board, valid_moves, player):
        if not valid_moves:
            return None

        best_value = -999
        best_move = None

        for move in valid_moves:
            # simulate board after this move
            new_board = self.apply_move(board, move, player)

            # convert to neural network input
            x = self.encode(new_board, player)

            # predict value
            with torch.no_grad():
                value = self.model(x).item()

            # choose max
            if value > best_value:
                best_value = value
                best_move = move

        return best_move
