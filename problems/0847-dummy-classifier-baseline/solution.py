import numpy as np
from collections import Counter
from math import floor

def dummy_classifier(y_train, n_test, strategy, constant=None):
    """
    Produce baseline predictions of length n_test using the given strategy.
    Returns a Python list of predicted labels.
    """
    if strategy == "most_frequent":
        counts = Counter(y_train)                                  
        best_class, _ = max(counts.items(),
                            key=lambda kv: (kv[1], -kv[0]))        
        return [best_class] * n_test                                

    elif strategy == "constant":
        return [constant] * n_test   

    elif strategy == "uniform":
        sorted_classes = sorted(set(y_train))
        k = len(sorted_classes)
        result = []
        for i in range(n_test):
            result.append(sorted_classes[i % k]) 
        return result

    elif strategy =="stratified":
        
        count = Counter(y_train)
        sorted_classes = sorted(count.keys())
        floors = {}
        fractions = {}
        for c in sorted_classes :
            
            count_c = count[c]
            f_c = count_c / len(y_train)
            raw = n_test * f_c
            floors[c] = floor(raw)
            fractions[c] = raw - floor(raw) 
            
        remaining = n_test - sum(floors.values())
             # Étape 4 : distribuer `remaining` aux plus grandes fractions
            #tie-break → plus petit label
        order = sorted(sorted_classes, key=lambda c : (-fractions[c], c))

        for c in order[:remaining]:                    # top `remaining`
            floors[c] += 1

            # Étape 5 : construire la sortie groupée par classe (ordre trié)
        result = []
        for c in sorted_classes:
            result.extend([c] * floors[c])
        return result
    

    
