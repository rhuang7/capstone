def check(candidate):
    assert candidate(["python (chrome)"])==("python")
    assert candidate(["string(.abc)"])==("string")
    assert candidate(["alpha(num)"])==("alpha")


def remove_parenthesis_area(s):
    result = ""
    in_paren = False
    for char in s:
        if char == '(':
            in_paren = True
        elif char == ')':
            in_paren = False
        else:
            if not in_paren:
                result += char
    return result

check(remove_parenthesis_area)