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
    
    # Precompute the maximum consecutive 1s for all possible rotations
    # Since the array is circular, we can double it and compute max consecutive 1s in a sliding window of size N
    double_A = A + A
    max_consec_ones = [0] * (N + 1)
    current = 0
    for i in range(len(double_A)):
        if double_A[i] == 1:
            current += 1
            if current > max_consec_ones[i % N]:
                max_consec_ones[i % N] = current
        else:
            current = 0
    
    # To handle rotation, we need to track the current rotation offset
    offset = 0
    
    for c in S:
        if c == '!':
            # Right shift the array
            offset = (offset + 1) % N
        else:
            # Find the maximum consecutive 1s in the current rotation
            # The maximum is min(max_consec_ones[i], K) for all i
            # But since we need the maximum that is <= K, we can just take the min
            max_len = 0
            for i in range(N):
                if max_consec_ones[i] <= K:
                    max_len = max(max_len, max_consec_ones[i])
            print(max_len)
    
if __name__ == '__main__':
    solve()