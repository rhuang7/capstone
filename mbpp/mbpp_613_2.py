def check(candidate):
    assert candidate([('key1', [3, 4, 5]), ('key2', [1, 4, 2]), ('key3', [9, 3])]) == [('key1', 5), ('key2', 4), ('key3', 9)]
    assert candidate([('key1', [4, 5, 6]), ('key2', [2, 5, 3]), ('key3', [10, 4])]) == [('key1', 6), ('key2', 5), ('key3', 10)]
    assert candidate([('key1', [5, 6, 7]), ('key2', [3, 6, 4]), ('key3', [11, 5])]) == [('key1', 7), ('key2', 6), ('key3', 11)]


def find_max_value_by_attribute(record_list, attribute):
    if not record_list:
        return None
    
    max_value = None
    for record in record_list:
        if isinstance(record, tuple) and len(record) > 0 and attribute < len(record):
            value = record[attribute]
            if isinstance(value, (int, float)):
                if max_value is None or value > max_value:
                    max_value = value
    return max_value

check(find_max_value_by_attribute)