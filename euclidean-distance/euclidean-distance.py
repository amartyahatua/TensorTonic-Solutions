import numpy as np
import math

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    result=0
    # Write code here
    for i in range(len(x)):
        result+=(x[i]-y[i])**2
    return math.sqrt(result)
        