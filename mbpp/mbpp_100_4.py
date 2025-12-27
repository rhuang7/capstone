def check(candidate):
    assert candidate(99)==101
    assert candidate(1221)==1331
    assert candidate(120)==121


def next_smallest_palindrome(n):
    def is_palindrome(num):
        return str(num) == str(num)[::-1]
    
    num = n
    while True:
        if is_palindrome(num):
            return num
        num += 1

check(next_smallest_palindrome)