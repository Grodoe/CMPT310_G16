# src/minimax_dataset.py
import torch
import numpy as np
from src.nn_utils import encode_board
from src.MiniMax import MinimaxAI
from src.utils import get_valid_moves
from src.rules import apply_move

class MinimaxDataset(torch.utils.data.Dataset):
    def __init__(self, num_positions=2000, depth=3, player=1):
        self.samples = []
        self.mm = MinimaxAI(depth=depth, player=player)

        for _ in range(num_positions):
            board = self.random_position()
            value = self.mm.minimax(board.copy(), depth, player, -9999, 9999)
            self.samples.append((board, value))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        board, value = self.samples[idx]
        x = encode_board(board, 1)     # always train from player=1 perspective
        y = torch.tensor([value], dtype=torch.float32)
        return x.squeeze(0), y

    def random_position(self):
        board = np.zeros((8, 8), dtype=int)
        # Fill with some random moves
        cur = 1
        for _ in range(np.random.randint(6, 22)):
            moves = get_valid_moves(board, cur)
            if not moves:
                cur *= -1
                continue
            r, c = moves[np.random.randint(len(moves))]
            apply_move(board, r, c, cur)
            cur *= -1
        return board
