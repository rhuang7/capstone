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
        
        # For each p_i, find the maximum number of times it can be used
        # to kill sorcerers
        max_kills = 0
        
        for val in p:
            # Find the maximum k such that val mod (N - k) == 0
            # We need to find the maximum k where val mod (N - k) == 0
            # and k <= N - 1 (since you can't kill yourself)
            # We can binary search for the maximum k
            low = 0
            high = N - 1
            best_k = 0
            
            while low <= high:
                mid = (low + high) // 2
                mod = val % (N - mid)
                if mod == 0:
                    best_k = mid
                    low = mid + 1
                else:
                    high = mid - 1
            
            max_kills += best_k
        
        results.append(str(max_kills))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()