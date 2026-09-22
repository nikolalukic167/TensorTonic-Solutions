import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here

    final = np.maximum(np.asarray(x, dtype=float), 0)

    return np.asarray(final)