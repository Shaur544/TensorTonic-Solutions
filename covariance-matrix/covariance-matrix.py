import numpy as np

def covariance_matrix(X):
    x= np.array(X)

    if x.ndim != 2:
        return None
    
    n, d = x.shape
    if n<2:
        return None

    mean = x.mean(axis= 0)
    X_centered = x - mean
    return (X_centered.T@ X_centered)/(n-1)
