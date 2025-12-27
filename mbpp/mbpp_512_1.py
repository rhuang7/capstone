def check(candidate):
    assert candidate((5, 6, (5, 6), 7, (8, 9), 9) ) == {5: 2, 6: 2, 7: 1, 8: 1, 9: 2}
    assert candidate((6, 7, (6, 7), 8, (9, 10), 10) ) == {6: 2, 7: 2, 8: 1, 9: 1, 10: 2}
    assert candidate((7, 8, (7, 8), 9, (10, 11), 11) ) == {7: 2, 8: 2, 9: 1, 10: 1, 11: 2}


def count_element_frequency(nested_tuple):
    from collections import defaultdict

    frequency = defaultdict(int)
    for element in nested_tuple:
        if isinstance(element, tuple):
            for sub_element in element:
                frequency[sub_element] += 1
        else:
            frequency[element] += 1
    return frequency

check(count_element_frequency)