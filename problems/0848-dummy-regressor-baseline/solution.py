import numpy as np

def dummy_regressor(y_train, n_test, strategy='mean', constant=None, quantile=None):
    """
    Baseline regressor that predicts a constant value derived from y_train.

    Args:
        y_train: 1D array-like of training target values.
        n_test: number of test predictions to return (int >= 0).
        strategy: one of 'mean', 'median', 'quantile', 'constant'.
        constant: required when strategy='constant'.
        quantile: required when strategy='quantile', must be in [0, 1].

    Returns:
        List[float] of length n_test, all equal to the chosen summary value.
    """
    
    if strategy == 'mean':
        p = np.mean(y_train)
        lst = [p]*n_test
        liste_float = [float(x) for x in lst]
        return liste_float

    elif strategy == 'median':
        p = np.median(y_train)
        lst = [p]*n_test
        liste_float = [float(x) for x in lst]
        return liste_float

    elif strategy == 'quantile':
        if quantile is None or not (0<=quantile<=1):
            raise ValueError
        p = np.quantile(y_train, quantile)
        lst = [p]*n_test
        liste_float = [float(x) for x in lst]
        return liste_float

    elif strategy == 'constant':
        if constant is None:
            raise ValueError
        p = constant
        lst = [p]*n_test
        liste_float = [float(x) for x in lst]
        return liste_float
    else: 
        raise ValueError













    pass
