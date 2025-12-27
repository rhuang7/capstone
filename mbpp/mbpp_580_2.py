def check(candidate):
    assert candidate((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert candidate((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert candidate((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)


def extract_even_elements(nested_tuple):
    result = []
    for item in nested_tuple:
        if isinstance(item, tuple):
            result.extend(extract_even_elements(item))
        elif isinstance(item, int) and item % 2 == 0:
            result.append(item)
    return result

check(extract_even_elements)