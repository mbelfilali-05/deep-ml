import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    # Your code here
    n,d = data.shape
    m= np.random.default_rng(seed).permutation(n)
    train_end = int(n * train_frac)
    validation_end = train_end + int(n * validation_frac)

    train_idx = m[:train_end]
    validation_idx = m[train_end: validation_end]
    test_idx = m[validation_end: ]

    train = data[train_idx]
    validation = data[validation_idx]
    test = data[test_idx]

    return [train, validation, test]
    
    
    
