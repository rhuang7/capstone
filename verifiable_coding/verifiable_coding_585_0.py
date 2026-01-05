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
            # The number of sorcerers that can be killed with this spell is
            # the number of times val can be subtracted from N, N-1, N-2, etc.
            # until it becomes less than the current number of sorcerers
            # This is equivalent to floor((N - 1) / val)
            # But we need to find the maximum k such that val * k <= N - 1
            # So k = floor((N - 1) / val)
            k = (N - 1) // val
            max_kills += k
        
        results.append(str(max_kills))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()