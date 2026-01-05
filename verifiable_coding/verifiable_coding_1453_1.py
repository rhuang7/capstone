import sys
import math

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
    
    # To handle rotations, we'll keep track of the current rotation offset
    # The array is circular, so we can represent it as a circular buffer
    # We'll use a deque to represent the current array
    from collections import deque
    dq = deque(A)
    offset = 0  # number of right shifts applied
    
    def get_current_array():
        # Return the current array as a list
        return list(dq)
    
    def get_current_prefix():
        # Return the current prefix sums of 1s
        arr = get_current_array()
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i+1] = prefix[i] + arr[i]
        return prefix
    
    def get_max_ones_in_window(prefix, K):
        max_len = 0
        for i in range(1, N+1):
            j = i + K - 1
            if j > N:
                break
            current = prefix[j] - prefix[i-1]
            if current > max_len:
                max_len = current
        return max_len
    
    for c in S:
        if c == '!':
            # Right shift the array
            # Remove the last element and add it to the front
            last = dq.pop()
            dq.appendleft(last)
            offset += 1
        else:
            # Query: find the max length of 1s in a window of size <= K
            # We need to compute the max length of consecutive 1s in the current array
            # Since the array is circular, we can concatenate it with itself and check
            # all windows of size up to K
            arr = get_current_array()
            # To handle circularity, we can double the array and check all windows
            # of size up to K
            max_len = 0
            for i in range(N):
                j = i + 1
                while j <= i + K and j < 2*N:
                    if arr[j % N] == 1:
                        j += 1
                    else:
                        break
                max_len = max(max_len, j - i)
            print(max_len)
    
if __name__ == '__main__':
    solve()