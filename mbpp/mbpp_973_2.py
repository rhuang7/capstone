def check(candidate):
    assert candidate("python",2) == "thonpy"   
    assert candidate("bigdata",3 ) == "databig" 
    assert candidate("hadoop",1 ) == "adooph" 


def left_rotate_string(s, n):
    if not s:
        return s
    n = n % len(s)  # Handle cases where n is larger than the string length
    return s[n:] + s[:n]

check(left_rotate_string)