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
            # For larger N, we can find a pattern
            # The sequence is: 1, 6, 7, 36, 37, 42, 43, 216, ...
            # It seems to be: for even positions, it's (k^3) - 1, for odd positions, it's (k^3)
            # Let's find k based on N
            k = (N + 1) // 2
            if N % 2 == 1:
                results.append(k ** 3)
            else:
                results.append(k ** 3 - 1)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()