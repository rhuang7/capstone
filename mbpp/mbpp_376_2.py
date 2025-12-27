def check(candidate):
    assert candidate((1, 1, 4, 4, 4, 5, 5, 6, 7, 7)) == (1, 'MSP', 4, 'MSP', 'MSP', 5, 'MSP', 6, 7, 'MSP')
    assert candidate((2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9)) == (2, 3, 4, 'MSP', 5, 6, 'MSP', 7, 8, 9, 'MSP')
    assert candidate((2, 2, 5, 4, 5, 7, 5, 6, 7, 7)) == (2, 'MSP', 5, 4, 'MSP', 7, 'MSP', 6, 'MSP', 'MSP')


def replace_duplicates_with_custom_value(tuples, custom_value):
    from collections import defaultdict

    element_count = defaultdict(int)
    result = []

    for t in tuples:
        if isinstance(t, tuple):
            for element in t:
                element_count[element] += 1

    for t in tuples:
        if isinstance(t, tuple):
            new_tuple = []
            for element in t:
                if element_count[element] > 1:
                    new_tuple.append(custom_value)
                else:
                    new_tuple.append(element)
            result.append(tuple(new_tuple))
    
    return result

check(replace_duplicates_with_custom_value)