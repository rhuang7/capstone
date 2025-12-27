def check(candidate):
    assert candidate([(None, 2), (None, None), (3, 4), (12, 3), (None, )] ) == '[(None, 2), (3, 4), (12, 3)]'
    assert candidate([(None, None), (None, None), (3, 6), (17, 3), (None,1 )] ) == '[(3, 6), (17, 3), (None, 1)]'
    assert candidate([(1, 2), (2, None), (3, None), (24, 3), (None, None )] ) == '[(1, 2), (2, None), (3, None), (24, 3)]'


def remove_all_none_tuples(tuples_list):
    return [t for t in tuples_list if not all(x is None for x in t)]

check(remove_all_none_tuples)