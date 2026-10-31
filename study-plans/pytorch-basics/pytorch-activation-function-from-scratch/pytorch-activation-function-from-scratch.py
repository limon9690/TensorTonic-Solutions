import torch

def activate(x: torch.Tensor, method: str = "relu") -> torch.Tensor:
    """
    Returns a float32 tensor with the same shape as x.
    """
    if method == 'relu':
        return torch.where(x > 0, x , 0)
    elif method == 'sigmoid':
        return (1 / (1 + torch.exp(-x)))
    elif method == 'tanh':
        return 2 / (1 + torch.exp(-2 * x)) - 1
    else:
        return torch.where(x > 0, x, x * 0.01)
