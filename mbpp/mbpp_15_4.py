def check(candidate):
    assert candidate("AbCd")==['bC','d']
    assert candidate("Python")==['y', 't', 'h', 'o', 'n']
    assert candidate("Programming")==['r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']


def split_at_lowercase(s):
    result = []
    i = 0
    while i < len(s):
        if s[i].islower():
            result.append(s[i])
            i += 1
        else:
            result.append(s[i:])
            break
    return result

check(split_at_lowercase)