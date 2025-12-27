def check(candidate):
    assert candidate(11,10,9) == 9
    assert candidate(5,7,4) == 2
    assert candidate(2,2,1) == 1


def find_max_periodic_value(function, period, num_samples):
    import numpy as np
    
    max_value = -np.inf
    for i in range(num_samples):
        x = i * period / num_samples
        current_value = function(x)
        if current_value > max_value:
            max_value = current_value
    return max_value

check(find_max_periodic_value)