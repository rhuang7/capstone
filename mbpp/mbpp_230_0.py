def check(candidate):
    assert candidate("hello people",'@')==("hello@people")
    assert candidate("python program language",'$')==("python$program$language")
    assert candidate("blank space","-")==("blank-space")


def replace_spaces(s, replacement):
    return s.replace(' ', replacement)

check(replace_spaces)