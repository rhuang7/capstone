def check(candidate):
    assert candidate('python') == ['p','y','t','h','o','n']
    assert candidate('Name') == ['N','a','m','e']
    assert candidate('program') == ['p','r','o','g','r','a','m']


def split_string_into_characters(s):
    return list(s)

check(split_string_into_characters)