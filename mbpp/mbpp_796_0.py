def check(candidate):
    assert candidate({'a': 100, 'b':200, 'c':300}) == 600
    assert candidate({'a': 25, 'b':18, 'c':45}) == 88
    assert candidate({'a': 36, 'b':39, 'c':49}) == 124


def sum_dictionary_values(d):
    return sum(d.values())

check(sum_dictionary_values)