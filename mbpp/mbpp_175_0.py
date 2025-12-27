def check(candidate):
    assert candidate("(){}[]")==True
    assert candidate("()[{)}")==False
    assert candidate("()")==True


def is_valid_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return not stack

check(is_valid_parentheses)