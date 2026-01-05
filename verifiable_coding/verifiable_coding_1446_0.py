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
        # But M ^ (M + 1) is a sequence of 1s in binary
        # So N must be of the form 2^k - 1
        # Check if N is of the form 2^k - 1
        if (N + 1) & N == 0:
            # N is of the form 2^k - 1
            k = (N + 1).bit_length()
            M = 1 << (k - 1)
            results.append(str(M))
        else:
            results.append("-1")
    print("\n".join(results))

if __name__ == '__main__':
    solve()