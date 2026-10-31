import torch


def reshape_tensor(x: torch. Tensor, op: str) -> torch. Tensor:
    """
    Returns the reshaped float32 tensor, including a scalar tensor after a complete squeeze.
    """
    res = None


    if op == 'flatten':
        res = torch.flatten(x)
    elif op == 'squeeze':
        res = torch.squeeze(x)
    else:
        res = x.T

    return res
        