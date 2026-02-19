import numpy as np

def linear_regression_closed_form(X, y):
    X= np.asarray(X)
    y= np.asarray(y)
    XT= X.T

    w= np.linalg.inv(XT @X) @XT @y
    return w
    pass