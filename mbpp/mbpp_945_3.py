def check(candidate):
    assert candidate(('x', 'y', 'z') ) == {'y', 'x', 'z'}
    assert candidate(('a', 'b', 'c') ) == {'c', 'a', 'b'}
    assert candidate(('z', 'd', 'e') ) == {'d', 'e', 'z'}


def convert_tuples_to_set(tuples):
    return set(tuples)

check(convert_tuples_to_set)