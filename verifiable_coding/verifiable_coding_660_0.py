import sys

def is_interesting(n):
    if n == 0:
        return 1
    digits = list(map(int, str(n)))
    fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    total = 0
    for d in digits:
        total += fact[d]
    return 1 if total == n else 0

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    for i in range(1, T + 1):
        N = int(data[i])
        print(is_interesting(N))

if __name__ == '__main__':
    solve()