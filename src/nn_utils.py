# src/nn_utils.py
import torch

def encode_board(board, current_player):
    """
    Encode board as:
    +1 = current player's pieces
    -1 = opponent pieces
     0 = empty
    """
    encoded = board * current_player   # flip colors so network always sees "my pieces" as +1
    tensor = torch.tensor(encoded, dtype=torch.float32)
    tensor = tensor.unsqueeze(0).unsqueeze(0)  # [batch=1, channel=1, 8,8]
    return tensor
