def check(candidate):
    assert candidate([('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)])== ({'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})
    assert candidate([('yellow', 10), ('blue', 20), ('yellow', 30), ('blue', 40), ('red', 10)])== ({'yellow': [10, 30], 'blue': [20, 40], 'red': [10]})
    assert candidate([('yellow', 15), ('blue', 25), ('yellow', 35), ('blue', 45), ('red', 15)])== ({'yellow': [15, 35], 'blue': [25, 45], 'red': [15]})


from collections import defaultdict

def group_key_value_pairs(pairs):
    grouped = defaultdict(list)
    for key, value in pairs:
        grouped[key].append(value)
    return dict(grouped)

check(group_key_value_pairs)