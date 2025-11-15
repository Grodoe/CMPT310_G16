# src/nn_model.py
import torch
import torch.nn as nn
import torch.nn.functional as F

class ReversiValueNet(nn.Module):
    def __init__(self):
        super().__init__()
        # Input = 8x8 board → flatten → feed into CNN
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(64 * 8 * 8, 128)
        self.fc2 = nn.Linear(128, 1)   # output = predicted value

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = x.reshape(x.size(0), -1)  # flatten
        x = F.relu(self.fc1(x))
        return torch.tanh(self.fc2(x))  # value in [-1, 1]
