def check(candidate):
    assert candidate(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((-5, -4), (1, -4), (1, 8), (-6, 7))
    assert candidate(((13, 4), (14, 6), (13, 10), (12, 11)), ((19, 8), (14, 10), (12, 2), (18, 4))) == ((-6, -4), (0, -4), (1, 8), (-6, 7))
    assert candidate(((19, 5), (18, 7), (19, 11), (17, 12)), ((12, 9), (17, 11), (13, 3), (19, 5))) == ((7, -4), (1, -4), (6, 8), (-2, 7))


def subtract_nested_tuples(t1, t2):
    def subtract_tuple(t1, t2):
        return tuple(a - b for a, b in zip(t1, t2))
    
    result = []
    for t in zip(t1, t2):
        result.append(subtract_tuple(t[0], t[1]))
    return tuple(result)

check(subtract_nested_tuples)