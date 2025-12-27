def check(candidate):
    assert candidate(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
    assert candidate(((2, 4), (5, 6), (3, 10), (2, 11)),((7, 8), (4, 10), (2, 2), (8, 4)) ) == ((14, 32), (20, 60), (6, 20), (16, 44))
    assert candidate(((3, 5), (6, 7), (4, 11), (3, 12)),((8, 9), (5, 11), (3, 3), (9, 5)) ) == ((24, 45), (30, 77), (12, 33), (27, 60))


def index_wise_multiplication(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Tuples must be of the same length for index-wise multiplication.")
    
    result = []
    for i in range(len(tuple1)):
        result.append(tuple1[i] * tuple2[i])
    return tuple(result)

check(index_wise_multiplication)