def check(candidate):
    assert candidate({'a': 100, 'b': 200},{'x': 300, 'y': 200})=={'x': 300, 'y': 200, 'a': 100, 'b': 200}
    assert candidate({'a':900,'b':900,'d':900},{'a':900,'b':900,'d':900})=={'a':900,'b':900,'d':900,'a':900,'b':900,'d':900}
    assert candidate({'a':10,'b':20},{'x':30,'y':40})=={'x':30,'y':40,'a':10,'b':20}


def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] = value
        else:
            merged[key] = value
    return merged

check(merge_dicts)