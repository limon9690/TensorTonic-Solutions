import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns sample variance and standard deviation as Python floats.
    """
    mean = np.mean(x)
    variance = 0

    for num in x:
        variance += (mean - num) ** 2

    variance = variance / (len(x)-1)
    std = np.sqrt(variance)

    return {'variance': float(variance), 'std_dev': float(std)}