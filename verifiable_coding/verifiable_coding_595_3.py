import sys

def is_palindrome(s):
    return s == s[::-1]

def solve():
    import sys
    input = sys.stdin.buffer.read().decode().strip()
    S = input
    n = len(S)
    total = 0

    for i in range(n):
        for j in range(i + 1, n):
            s1 = S[i:j]
            s2 = S[j:]
            if is_palindrome(s1 + s2):
                total += 1

    print(total)

if __name__ == '__main__':
    solve()