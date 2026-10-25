import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns the requested percentiles as a float64 array.
    """
    res = np.percentile(x, q, method='linear')

    return res