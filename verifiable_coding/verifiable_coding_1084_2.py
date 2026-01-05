import sys

def solve():
    S = sys.stdin.buffer.read().decode().strip()
    n = len(S)
    res = 0
    current = 0
    for i in range(n):
        if S[i] == '1':
            current += 1
        else:
            if current > 0:
                res += 1
                current = 0
    print(res)

if __name__ == '__main__':
    solve()