def check(candidate):
    assert candidate("{()}[{}]") == True
    assert candidate("{()}[{]") == False
    assert candidate("{()}[{}][]({})") == True


def is_balanced(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return not stack

check(is_balanced)