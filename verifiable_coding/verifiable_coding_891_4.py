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
    # Since a must be in [1, N], then q - b must be in [1, N]
    # => b must be in [q - N, q - 1]
    # Also, b must be in [N+1, 2N]
    # So the valid range for b is [max(N+1, q - N), min(2N, q - 1)]
    # The number of valid b is max(0, min(2N, q - 1) - max(N+1, q - N) + 1)
    
    for q in queries:
        low = max(N + 1, q - N)
        high = min(2 * N, q - 1)
        if low > high:
            print(0)
        else:
            print(high - low + 1)
            
if __name__ == '__main__':
    solve()