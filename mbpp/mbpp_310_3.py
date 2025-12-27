def check(candidate):
    assert candidate("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
    assert candidate("item1")==('i', 't', 'e', 'm', '1')
    assert candidate("15.10")==('1', '5', '.', '1', '0')


def string_to_tuple(s):
    return tuple(s)

check(string_to_tuple)