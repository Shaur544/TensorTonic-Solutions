import numpy as np

def calculate_eigenvalues(matrix):
    try:
        mat= np.array(matrix, dtype= float)
    except:
        return None
    
    if mat.ndim!=2 or mat.shape[0] != mat.shape[1]:
        return None
    
    if mat.size== 0:
        return None
    
    eig=np.linalg.eigvals(mat)

    idx= np.lexsort((eig.imag, eig.real))
    eig= eig[idx]
    return eig