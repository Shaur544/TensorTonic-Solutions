import numpy as np

def pearson_correlation(X):
    try:
        x= np.array(X, dtype = float)
    except:
        return None

    if x.ndim!=2 or x.shape[0]<2:
        return None
    n =x.shape[0]

    xc= x-np.mean(x, axis=0)

    cov= (xc.T @ xc)/ (n-1)

    std= np.std(x, axis= 0, ddof=1)

    denom= np.outer(std, std)

    corr = np.divide(cov, denom, out=np.zeros_like(cov), where=denom != 0)

    corr[denom==0] = np.nan
    np.fill_diagonal(corr,1.0)
    return corr
