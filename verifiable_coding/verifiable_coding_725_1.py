import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, K, M = map(int, data[idx:idx+3])
        idx += 3
        R = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Try all possible ways to increase some elements by 1 (at most once)
        # Since N is small (<=17), we can try all combinations
        from itertools import combinations
        
        # Check if current configuration is valid
        def is_valid(R):
            for i in range(N - K + 1):
                sub = R[i:i+K]
                max_val = max(sub)
                count = sum(1 for x in sub if x == max_val)
                if count >= M:
                    return False
            return True
        
        # Try all possible ways to increase elements
        min_ops = float('inf')
        for mask in range(1 << N):
            new_R = R[:]
            ops = 0
            for i in range(N):
                if mask & (1 << i):
                    new_R[i] += 1
                    ops += 1
            if is_valid(new_R):
                min_ops = min(min_ops, ops)
        
        if min_ops != float('inf'):
            results.append(str(min_ops))
        else:
            results.append('-1')
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()