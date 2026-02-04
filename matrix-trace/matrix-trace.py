import numpy as np

def matrix_trace(A):
    A = np.array(A)
    trace = 0
    n = min(A.shape[0], A.shape[1])

    for i in range(n):
        trace += A[i][i]
    return float(trace)