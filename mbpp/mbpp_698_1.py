def check(candidate):
    assert candidate({(5, 6) : 3, (2, 3) : 9, (8, 4): 10, (6, 4): 12} ) == {(2, 3): 9, (6, 4): 12, (5, 6): 3, (8, 4): 10}
    assert candidate({(6, 7) : 4, (3, 4) : 10, (9, 5): 11, (7, 5): 13} ) == {(3, 4): 10, (7, 5): 13, (6, 7): 4, (9, 5): 11}
    assert candidate({(7, 8) : 5, (4, 5) : 11, (10, 6): 12, (8, 6): 14} ) == {(4, 5): 11, (8, 6): 14, (7, 8): 5, (10, 6): 12}


def sort_dict_by_key_product(d):
    def key_product(k):
        return k[0] * k[1]
    
    sorted_items = sorted(d.items(), key=key_product)
    return dict(sorted_items)

check(sort_dict_by_key_product)