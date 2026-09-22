import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    array = np.asarray(x, dtype=float)
    final = 1 / (1 + np.exp(-array))
    return final