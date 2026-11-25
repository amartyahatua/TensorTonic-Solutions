import numpy as np
import math
def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
   # 1. Handle single scalar inputs (int or float, excluding bool)
    if isinstance(x, (int, float)) and not isinstance(x, bool):
        return float(1 / (1 + np.exp(-x)))

    # 2. Handle list inputs (1D, 2D like [[-1, 0], [1, 2]], or higher)
    if isinstance(x, list):
        try:
            arr = np.asarray(x)
        except ValueError:
            # Catches jagged lists with uneven row lengths like [[-1, 0], [1]]
            raise TypeError("Input list must have uniform dimensions.")

        # Verify array is non-empty and contains only numeric types (no strings/bools/objects)
        if arr.size > 0 and (
            np.issubdtype(arr.dtype, np.floating) or np.issubdtype(arr.dtype, np.integer)
        ):
            return 1 / (1 + np.exp(-arr.astype(np.float64)))

    raise TypeError("Input 'x' must be a number or a non-empty rectangular list of numbers.")
        
    #return sigmoid_result