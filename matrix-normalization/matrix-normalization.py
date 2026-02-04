import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    try:
        mat = np.array(matrix, dtype= float)
    except:
        return None
    
    if mat.ndim!= 2:
        return None
    
    if norm_type== 'l1':
        norm = np.sum(np.abs(mat), axis = axis, keepdims= True)
    elif norm_type=='l2':
        norm = np.sqrt(np.sum(mat **2, axis= axis, keepdims= True))
    elif norm_type=='max':
        norm =np.max(np.abs(mat), axis = axis, keepdims=True)
    else: return None

    norm[norm==0]=1

    return mat/norm