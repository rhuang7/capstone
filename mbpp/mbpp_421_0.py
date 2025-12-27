def check(candidate):
    assert candidate(("ID", "is", 4, "UTS") ) == 'ID-is-4-UTS'
    assert candidate(("QWE", "is", 4, "RTY") ) == 'QWE-is-4-RTY'
    assert candidate(("ZEN", "is", 4, "OP") ) == 'ZEN-is-4-OP'


def concatenate_tuple_elements(tup, delimiter):
    return delimiter.join(tup)

check(concatenate_tuple_elements)