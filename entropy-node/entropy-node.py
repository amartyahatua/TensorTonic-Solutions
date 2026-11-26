import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    result=0
    vals, counts=np.unique(y, return_counts=True)
    print(vals)
    print(counts)
    class_prob=counts/len(y)
    
    for i in range(len(counts)):
        result+= class_prob[i]*np.log2(class_prob[i])

    return -float(result)
        