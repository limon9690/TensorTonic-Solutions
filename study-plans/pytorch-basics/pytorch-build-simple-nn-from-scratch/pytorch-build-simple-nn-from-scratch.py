import torch
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self, in_features: int, hidden_size: int, out_features: int):
        super().__init__()
        self.linear = nn.Linear(in_features, hidden_size)
        self.relu = nn.ReLU()
        self.out = nn.Linear(hidden_size, out_features)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Returns a float32 tensor of shape (batch, out_features).
        """
        res = self.linear(x)
        res = self.relu(res)
        res = self.out(res)

        return res
