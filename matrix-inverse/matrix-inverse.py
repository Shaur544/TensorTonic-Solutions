import numpy as np

def matrix_inverse(A):
    try:
        mat = np.array(A, dtype = float)
    except:
        return None

    if mat.ndim != 2 or mat.shape[0] != mat.shape[1]:
        return None
    if abs(np.linalg.det(mat))< 1e-10:
        return None
    return np.linalg.inv(mat)

    
    
