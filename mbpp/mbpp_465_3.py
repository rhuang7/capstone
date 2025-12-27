def check(candidate):
    assert candidate({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
    assert candidate({'c1': 'Red', 'c2': None, 'c3':None})=={'c1': 'Red'}
    assert candidate({'c1': None, 'c2': 'Green', 'c3':None})=={ 'c2': 'Green'}


def drop_empty_items(d):
    return {k: v for k, v in d.items() if v}

check(drop_empty_items)