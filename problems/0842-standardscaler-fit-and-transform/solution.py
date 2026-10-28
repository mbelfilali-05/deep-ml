import numpy as np

def standard_scaler(X_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    """
    Fit a standard scaler on X_train and transform X_test.
    Returns the standardized X_test as a numpy array.
    """
    moy = np.mean(X_train, axis = 0)
    stdr = np.std(X_train, axis =0)
    for i in range(len(stdr)):
        if stdr[i]==0:
            stdr[i]=1
    
    std_train = (X_test -moy)/stdr
    return std_train


