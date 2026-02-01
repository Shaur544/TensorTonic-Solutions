import numpy as np

def make_diagonal(v):
    n = len(v)
    v= np.array(v)
    t = np.zeros((n,n), dtype= v.dtype)

    for i in range(n):
        t[i][i] = v[i]
    return t