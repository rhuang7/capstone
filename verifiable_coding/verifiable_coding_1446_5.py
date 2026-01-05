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
        # M ^ (M + 1) = (M | (M + 1)) - (M & (M + 1))
        # Since M and M+1 are consecutive, their binary representations differ in the least significant 1 bit.
        # So M ^ (M + 1) is a number with a single 1 followed by zeros.
        # Therefore, N must be of the form 2^k - 1, where k is a positive integer.
        # Check if N + 1 is a power of two
        if (N + 1) & (N) == 0:
            # N + 1 is a power of two
            # The smallest M is (N + 1) >> 1
            M = (N + 1) >> 1
            results.append(str(M))
        else:
            results.append("-1")
    print("\n".join(results))

if __name__ == '__main__':
    solve()