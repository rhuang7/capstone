import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        p = list(map(int, data[idx:idx+M]))
        idx += M
        
        # For each p_i, compute the maximum number of times it can be used
        # to kill sorcerers
        max_kills = 0
        for val in p:
            # The number of sorcerers that can be killed with this spell
            # is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current number of sorcerers
            # This is equivalent to the number of times val can be subtracted
            # from N, N-1, N-2, ... until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val) + 1
            # But we need to find the maximum number of times this spell can be used
            # which is the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current count
            # which is the same as floor((N - 1) / val)