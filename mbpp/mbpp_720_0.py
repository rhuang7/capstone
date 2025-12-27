def check(candidate):
    assert candidate((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
    assert candidate((1, 2, 3), {"UTS" : 2, "is" : 3, "Worst" : 4} ) == (1, 2, 3, {'UTS': 2, 'is': 3, 'Worst': 4})
    assert candidate((8, 9, 10), {"POS" : 3, "is" : 4, "Okay" : 5} ) == (8, 9, 10, {'POS': 3, 'is': 4, 'Okay': 5})


def add_dict_to_tuple(tup, d):
    return tup + (d,)

check(add_dict_to_tuple)