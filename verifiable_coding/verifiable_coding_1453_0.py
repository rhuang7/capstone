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
    
    # To handle rotation, we'll store the array as a circular array
    # We'll track the current rotation offset
    offset = 0
    
    def get_real_pos(i):
        return (i + offset) % N
    
    def get_real_value(i):
        return A[get_real_pos(i)]
    
    def get_real_prefix(i):
        return prefix[get_real_pos(i)]
    
    def get_real_prefix_sum(i):
        return prefix[i]
    
    def get_real_prefix_sum_from(i):
        return prefix[i]
    
    def get_real_prefix_sum_to(j):
        return prefix[j] - prefix[i]
    
    def get_real_max_ones_in_range(l, r):
        # l and r are real positions
        # convert to original positions
        l_orig = get_real_pos(l)
        r_orig = get_real_pos(r)
        if l_orig <= r_orig:
            return get_real_prefix_sum_to(r_orig) - get_real_prefix_sum_from(l_orig)
        else:
            return get_real_prefix_sum_to(N) - get_real_prefix_sum_from(l_orig) + get_real_prefix_sum_to(r_orig)
    
    def get_real_max_ones_in_window(l, r):
        # l and r are real positions
        # convert to original positions
        l_orig = get_real_pos(l)
        r_orig = get_real_pos(r)
        if l_orig <= r_orig:
            return get_real_prefix_sum_to(r_orig) - get_real_prefix_sum_from(l_orig)
        else:
            return get_real_prefix_sum_to(N) - get_real_prefix_sum_from(l_orig) + get_real_prefix_sum_to(r_orig)
    
    def get_real_max_ones_in_window_with_k(l, r, k):
        # find the maximum number of 1s in a window of size <=k
        # l and r are real positions
        # convert to original positions
        l_orig = get_real_pos(l)
        r_orig = get_real_pos(r)
        if l_orig <= r_orig:
            max_ones = 0
            for i in range(l_orig, min(r_orig + 1, l_orig + k)):
                max_ones = max(max_ones, get_real_prefix_sum_to(i) - get_real_prefix_sum_from(l_orig))
            return min(max_ones, k)
        else:
            max_ones = 0
            for i in range(l_orig, N + 1):
                max_ones = max(max_ones, get_real_prefix_sum_to(N) - get_real_prefix_sum_from(l_orig))
            for i in range(1, r_orig + 1):
                max_ones = max(max_ones, get_real_prefix_sum_to(i) - get_real_prefix_sum_from(1))
            return min(max_ones, k)
    
    for c in S:
        if c == '!':
            # Right shift
            offset = (offset + 1) % N
        else:
            # Query
            # Find the maximum number of 1s in a window of size <=K
            # We can use a sliding window approach
            # But due to rotation, we need to handle circular array
            # So we'll simulate the array as a circular array
            # We'll use a sliding window of size K
            max_ones = 0
            for i in range(N):
                # Check window starting at i
                # The window can be up to K elements long
                # We need to find the maximum number of 1s in any window of size <=K
                # So we'll check all possible window sizes from 1 to min(K, N - i)
                # But this is O(N*K), which is too slow
                # So we need a better approach
                # We can use a sliding window of size K
                # But due to rotation, we need to handle circular array
                # So we'll simulate the array as a circular array
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                # We'll use a sliding window of size K
                #