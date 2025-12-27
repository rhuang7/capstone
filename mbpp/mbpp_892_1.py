def check(candidate):
    assert candidate('python  program')==('python program')
    assert candidate('python   programming    language')==('python programming language')
    assert candidate('python                     program')==('python program')


def remove_multiple_spaces(s):
    return ' '.join(s.split())

check(remove_multiple_spaces)