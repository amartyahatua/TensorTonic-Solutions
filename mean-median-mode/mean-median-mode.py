from collections import Counter
import numpy as np
import math
def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean = sum(x)/len(x)
    x_sort = sorted(x)
    
    if len(x)%2 == 0:
        mid_left = int((len(x)/2)-1)
        mid_right = mid_left+1
        median = float((x_sort[mid_left]+x_sort[mid_right])/2)
    else:
        mid_index = math.floor(len(x)/2)
        print("mid_index: ",mid_index)
        median = float(x_sort[mid_index])

    vals, counts = np.unique(x, return_counts=True, sorted=True)
    return {'mean':mean, 'median':median, 'mode':float(vals[np.argmax(counts)])}