def check(candidate):
    assert candidate(("python 3.0")) == ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
    assert candidate(("bigdata")) == ('b', 'i', 'g', 'd', 'a', 't', 'a')
    assert candidate(("language")) == ('l', 'a', 'n', 'g', 'u', 'a', 'g','e')


def list_to_tuple(string_list):
    return tuple(string_list)

check(list_to_tuple)