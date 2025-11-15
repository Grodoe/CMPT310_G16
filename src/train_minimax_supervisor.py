# train_minimax_supervisor.py
import torch
from torch.utils.data import DataLoader
from src.nn_model import ReversiValueNet
from src.minimax_dataset import MinimaxDataset

device = "cuda" if torch.cuda.is_available() else "cpu"

# 1. Load dataset generated from minimax
dataset = MinimaxDataset(num_positions=3000, depth=3)
loader = DataLoader(dataset, batch_size=32, shuffle=True)

# 2. Create neural network
model = ReversiValueNet().to(device)

# 3. Loss + optimizer
criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

# 4. Training loop
for epoch in range(20):
    total_loss = 0
    for x, y in loader:
        x = x.to(device)
        y = y.to(device)

        pred = model(x).squeeze()

        loss = criterion(pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1}: Loss = {total_loss:.3f}")

# 5. Save model
torch.save(model.state_dict(), "model_minimax_supervised.pth")
print("Model saved.")
