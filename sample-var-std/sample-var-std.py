import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    variance = 0
    sd = 0
    x_bar = np.mean(x)
    temp = 0
    for i in range(len(x)):
        temp+=(x[i]-x_bar)**2
    variance = float(temp/(len(x)-1))
    sd = float(np.sqrt(variance))
    result = {'variance':variance, 'standard_deviation':sd}

    return result
        