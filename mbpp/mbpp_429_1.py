def check(candidate):
    assert candidate((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
    assert candidate((1, 2, 3, 4), (5, 6, 7, 8)) == (1, 2, 3, 0)
    assert candidate((8, 9, 11, 12), (7, 13, 14, 17)) == (0, 9, 10, 0)


def extract_elementwise_and_tuples(t1, t2):
    # Check if both tuples have the same length
    if len(t1) != len(t2):
        raise ValueError("Tuples must be of the same length")
    
    # Extract element-wise pairs as tuples
    elementwise_pairs = tuple(zip(t1, t2))
    
    # Extract individual elements as separate tuples
    element1_tuple = tuple(t1)
    element2_tuple = tuple(t2)
    
    return elementwise_pairs, element1_tuple, element2_tuple

check(extract_elementwise_and_tuples)