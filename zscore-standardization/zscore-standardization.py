import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    # Write code here
    mean = np.mean(np.asarray(X), axis=axis, keepdims=True)
    std = np.std(np.asarray(X), axis=axis, keepdims=True)
    
    # Replace small stds with 1.0 temporarily to prevent division-by-zero warnings
    safe_std = np.where(std <= eps, 1.0, std)
    normalized = (np.asarray(X) - mean) / safe_std
    
    # Return zeros wherever the original std was at most eps
    return np.where(std <= eps, 0.0, normalized)
    