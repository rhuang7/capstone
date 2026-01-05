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
        prefix[i + 1] = prefix[i] + A[i]
    
    # To handle rotation, we'll keep track of the rotation offset
    rotation = 0
    
    def get_pos(i):
        return (i + rotation) % N
    
    def get_val(i):
        return A[get_pos(i)]
    
    def get_prefix(i):
        return prefix[get_pos(i)]
    
    def get_prefix_sum(l, r):
        # Convert to original positions
        l_orig = (l + rotation) % N
        r_orig = (r + rotation) % N
        if l_orig > r_orig:
            return get_prefix(r_orig + 1) + get_prefix(N) - get_prefix(l_orig)
        else:
            return get_prefix(r_orig + 1) - get_prefix(l_orig)
    
    def max_ones_in_window(l, r):
        # Find the maximum number of 1s in any window of size <= K
        # We use a sliding window approach
        max_ones = 0
        current = 0
        left = l
        for right in range(l, r + 1):
            current += get_val(right)
            if right - left + 1 > K:
                current -= get_val(left)
                left += 1
            max_ones = max(max_ones, current)
        return max_ones
    
    for c in S:
        if c == '!':
            rotation = (rotation + 1) % N
        else:
            # Query: find max contiguous 1s <= K
            # We need to check the entire array
            max_ones = 0
            current = 0
            left = 0
            for right in range(N):
                current += get_val(right)
                if right - left + 1 > K:
                    current -= get_val(left)
                    left += 1
                max_ones = max(max_ones, current)
            print(max_ones)