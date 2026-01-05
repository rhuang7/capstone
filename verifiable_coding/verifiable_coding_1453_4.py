import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1
    K = int(data[idx])
    idx += 1
    
    A = list(map(int, data[idx:idx+N]))
    idx += N
    S = data[idx]
    
    # Precompute prefix sums of 1s
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + A[i]
    
    # To handle rotations, we can represent the array as a circular array
    # and track the current rotation offset
    offset = 0
    
    def get_real_pos(i):
        return (i + offset) % N
    
    def get_real_prefix(i):
        return prefix[(i + offset) % N]
    
    def get_real_value(i):
        return A[(i + offset) % N]
    
    def get_max_consecutive_ones():
        max_len = 0
        current = 0
        for i in range(N):
            if get_real_value(i) == 1:
                current += 1
                max_len = max(max_len, current)
            else:
                current = 0
        return min(max_len, K)
    
    for c in S:
        if c == '!':
            # Right shift
            offset = (offset + 1) % N
        else:
            # Query
            res = get_max_consecutive_ones()
            print(res)
    
if __name__ == '__main__':
    solve()