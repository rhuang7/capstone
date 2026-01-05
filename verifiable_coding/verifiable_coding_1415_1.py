import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]

    def is_palindrome(s):
        return s == s[::-1]

    def can_be_palindrome(s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Check if deleting left or right character makes it a palindrome
                return is_palindrome(s[left+1:right+1]) or is_palindrome(s[left:right])
            left += 1
            right -= 1
        return True

    for s in cases:
        if can_be_palindrome(s):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()