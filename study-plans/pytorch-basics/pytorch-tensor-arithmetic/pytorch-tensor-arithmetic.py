import torch

def tensor_op(x: torch.Tensor, y: torch.Tensor, op: str) -> torch.Tensor:
    """
    Returns the operation result as a float32 tensor.
    """
    res = None

    if op == 'add':
        res = torch.add(x, y)
    elif op == 'multiply':
        res = torch.mul(x, y)
    elif op == 'matmul':
        res = torch.matmul(x, y)
    elif op == 'power':
        res = torch.pow(x, y)
    else:
        res = torch.max(x, y)

    return res
        
