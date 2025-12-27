def check(candidate):
    assert candidate("python programming")==['python','programming']
    assert candidate("lists tuples strings")==['lists','tuples','strings']
    assert candidate("write a program")==['write','a','program']


def string_to_list(s):
    return list(s)

check(string_to_list)