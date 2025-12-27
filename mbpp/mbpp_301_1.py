def check(candidate):
    assert candidate({'a':1, 'b': {'c': {'d': {}}}})==4
    assert candidate({'a':1, 'b': {'c':'python'}})==2
    assert candidate({1: 'Sun', 2: {3: {4:'Mon'}}})==3


def dict_depth(d):
    if not isinstance(d, dict) or not d:
        return 0
    max_depth = 0
    for value in d.values():
        if isinstance(value, dict):
            current_depth = 1 + dict_depth(value)
            if current_depth > max_depth:
                max_depth = current_depth
    return max_depth

check(dict_depth)