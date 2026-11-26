import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    result = 0
    # Write code here
    for i in range(len(x)):
        result += np.abs(x[i]-y[i])

    return float(result)
        