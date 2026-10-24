import torch

def create_tensor(method: str, shape: list, value: float = 0.0) -> torch.Tensor:
    """
    Returns a float32 tensor with the requested shape.
    """
    res = None

    if method == 'zeros':
        res = torch.zeros(tuple(shape), dtype=torch.float32)
    elif method == 'ones':
        res = torch.ones(tuple(shape), dtype=torch.float32)
    else:
        res = torch.full(tuple(shape), value, dtype=torch.float32)

    return res
