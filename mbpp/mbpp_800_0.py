def check(candidate):
    assert candidate('python  program')==('pythonprogram')
    assert candidate('python   programming    language')==('pythonprogramminglanguage')
    assert candidate('python                     program')==('pythonprogram')


def remove_whitespaces(s):
    return s.replace(" ", "")

check(remove_whitespaces)