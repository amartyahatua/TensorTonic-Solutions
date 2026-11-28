import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x = np.asarray(x)
    x_zero = x
    x_zero = 0
    return np.maximum(x_zero,x)