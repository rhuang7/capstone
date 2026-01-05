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
        
        # Function to check if a given R is valid
        def is_valid(R):
            for i in range(N - K + 1):
                sub = R[i:i+K]
                max_val = max(sub)
                count = 0
                for j in range(K):
                    if sub[j] == max_val:
                        count += 1
                if count >= M:
                    return False
            return True
        
        # Try all possible ways to increase some elements by 1
        from itertools import product
        from collections import deque
        
        # We can only increase each element at most once
        # So we try all possible combinations of which elements to increase
        # Since N <= 17, 2^17 is 131072 which is manageable
        min_ops = float('inf')
        for mask in product([0, 1], repeat=N):
            new_R = []
            ops = 0
            for i in range(N):
                if mask[i]:
                    new_R.append(R[i] + 1)
                    ops += 1
                else:
                    new_R.append(R[i])
            if is_valid(new_R):
                min_ops = min(min_ops, ops)
        
        if min_ops == float('inf'):
            results.append(-1)
        else:
            results.append(min_ops)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()