import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = int(data[i])
        M = -1
        # Try all possible M up to a reasonable limit
        for m in range(1, 1 << 20):
            if (m ^ (m + 1)) == N:
                M = m
                break
        results.append(str(M))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()