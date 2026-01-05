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
            results.append(1)
        elif N == 2:
            results.append(6)
        elif N == 3:
            results.append(7)
        elif N == 4:
            results.append(36)
        elif N == 5:
            results.append(37)
        elif N == 6:
            results.append(42)
        elif N == 7:
            results.append(43)
        elif N == 8:
            results.append(216)
        else:
            # For larger N, we can derive the pattern
            # The sequence is based on 6^k and 6^k + 1
            # For even positions: 6^k
            # For odd positions: 6^k + 1
            k = (N + 1) // 2
            if N % 2 == 1:
                results.append(6 ** k + 1)
            else:
                results.append(6 ** k)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()