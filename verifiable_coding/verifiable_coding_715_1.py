import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().decode().split()
    s = input[0]
    n = len(s)
    res = 0
    for i in range(n):
        res += (ord(s[i]) - ord('A') + 1) * (26 ** (n - i - 1))
    print(res)

if __name__ == '__main__':
    solve()