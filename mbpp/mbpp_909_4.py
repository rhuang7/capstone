def check(candidate):
    assert candidate(99)==88
    assert candidate(1221)==1111
    assert candidate(120)==111


def is_palindrome(n):
    return str(n) == str(n)[::-1]

def previous_palindrome(n):
    while True:
        n -= 1
        if is_palindrome(n):
            return n

check(previous_palindrome)