def check(candidate):
    assert candidate("mnm") == 1
    assert candidate("abcda") == 3
    assert candidate("abcb") == 2


def minimize_string(s):
    if len(s) <= 1:
        return s
    
    for i in range(len(s) - 1):
        # Remove the i-th character and check if the resulting string is shorter
        new_s = s[:i] + s[i+1:]
        if len(new_s) < len(s):
            return new_s
    
    # If no single removal reduces the length, return the original string
    return s

check(minimize_string)