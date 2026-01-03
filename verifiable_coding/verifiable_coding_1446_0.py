import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = int(data[i])
        # Find the smallest M such that M ^ (M + 1) = N
        # M ^ (M + 1) = (M | (M + 1)) - (M & (M + 1)) = (M | (M + 1)) - (M & (M + 1))
        # But since M and M+1 are consecutive, their binary representations differ in the least significant 1 bit
        # So M ^ (M + 1) is a number with a single 1 followed by zeros
        # So N must be a number with a single 1 in its binary representation
        # Check if N is a power of two
        if (N & (N - 1)) != 0:
            results.append(-1)
            continue
        # If N is a power of two, then M is N >> 1
        results.append(N >> 1)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()