def check(candidate):
    assert candidate("My Name is Dawood") == 'My%20Name%20is%20Dawood'
    assert candidate("I am a Programmer") == 'I%20am%20a%20Programmer'
    assert candidate("I love Coding") == 'I%20love%20Coding'


def replace_spaces_with_percent20(s):
    return s.replace(' ', '%20')

check(replace_spaces_with_percent20)