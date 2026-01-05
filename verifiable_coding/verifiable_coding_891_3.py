import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    queries = list(map(int, data[2:2+M]))
    
    # For each query q, find the number of pairs (a, b) such that a + b = q
    # a is in [1, N], b is in [N+1, 2N]
    # a + b = q => a = q - b
    # Since a must be in [1, N], and b is in [N+1, 2N], we can find the valid range of b
    # For a to be in [1, N], q - b must be in [1, N]
    # => q - N <= b <= q - 1
    # Also, b must be in [N+1, 2N]
    # So the valid range of b is [max(N+1, q - N), min(2N, q - 1)]
    # The number of valid b's is max(0, min(2N, q - 1) - max(N+1, q - N) + 1)
    
    results = []
    for q in queries:
        lower = max(N + 1, q - N)
        upper = min(2 * N, q - 1)
        if lower > upper:
            results.append(0)
        else:
            results.append(upper - lower + 1)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()