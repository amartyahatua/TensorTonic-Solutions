import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    if sum(a)==0 or sum(b)==0:
        return 0.0
    else:
        a = np.asarray(a)
        b = np.asarray(b)
        dot_result = np.dot(a, b)
        norm = np.linalg.norm(a)*np.linalg.norm(b)
        return (dot_result/norm)
        