import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = int(data[i])
        if N == 1:
            results.append('1')
        else:
            # The sequence alternates between two patterns
            # For odd positions: (3^k - 1) / 2
            # For even positions: (3^k - 1) / 2 * 6 + 1
            # Where k is the number of times 2 fits into the position
            k = 0
            while (3 ** (k + 1) - 1) // 2 < N:
                k += 1
            if N % 2 == 1:
                res = (3 ** (k + 1) - 1) // 2
            else:
                res = (3 ** (k + 1) - 1) // 2 * 6 + 1
            results.append(str(res))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()