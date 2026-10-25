import numpy as np
from collections import Counter

def mean_median_mode(x: list) -> dict:
    """
    Returns mean, median, and mode as Python floats in a dictionary.
    """
    mean = np.mean(x)
    median = np.median(x)
    counts = Counter(x)
    mode_count = 0
    mode = float('-inf')
    
    for key, value in counts.items():
        if value > mode_count:
            mode_count = value
            mode = key 
        elif value == mode_count:
            mode = key if key < mode else mode


    return {'mean': float(mean), 'median': float(median), 'mode': float(mode)}
    
    

    