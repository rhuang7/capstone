def check(candidate):
    assert candidate({'a': 100, 'b': 200, 'c':300},{'a': 300, 'b': 200, 'd':400})==({'b': 400, 'd': 400, 'a': 400, 'c': 300}) 
    assert candidate({'a': 500, 'b': 700, 'c':900},{'a': 500, 'b': 600, 'd':900})==({'b': 1300, 'd': 900, 'a': 1000, 'c': 900}) 
    assert candidate({'a':900,'b':900,'d':900},{'a':900,'b':900,'d':900})==({'b': 1800, 'd': 1800, 'a': 1800})


def combine_dicts(d1, d2):
    combined = d1.copy()
    for key, value in d2.items():
        if key in combined:
            combined[key] += value
        else:
            combined[key] = value
    return combined

check(combine_dicts)