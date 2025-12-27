def check(candidate):
    assert candidate('python  @#&^%$*program123')==('pythonprogram123')
    assert candidate('python %^$@!^&*()  programming24%$^^()    language')==('pythonprogramming24language')
    assert candidate('python   ^%&^()(+_)(_^&67)                  program')==('python67program')


def remove_non_alphanumeric(s):
    import re
    return re.sub(r'[^a-zA-Z0-9]', '', s)

check(remove_non_alphanumeric)