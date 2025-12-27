def check(candidate):
    assert candidate("letstdlenstdporstd") == 3
    assert candidate("truststdsolensporsd") == 1
    assert candidate("makestdsostdworthit") == 2


def count_std_occurrences(s):
    count = 0
    i = 0
    while i < len(s) - 2:
        if s[i:i+3] == 'std':
            count += 1
            i += 3
        else:
            i += 1
    return count

check(count_std_occurrences)