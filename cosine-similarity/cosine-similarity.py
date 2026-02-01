import numpy as np

def cosine_similarity(a, b):
    a= np.array(a, dtype= float)
    b= np.array(b, dtype= float)

    norm_a= np.linalg.norm(a)
    norm_b= np.linalg.norm(b)
    
    if norm_a==0 or norm_b==0:
        return 0.0

    dot = float(np.dot(a, b))

    return dot/(norm_a*norm_b)