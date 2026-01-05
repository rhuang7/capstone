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
        N = int(data[idx])
        K = int(data[idx+1])
        M = int(data[idx+2])
        idx += 3
        R = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Check if it's possible to avoid arrest
        def is_possible(R):
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
        
        # Try all possible operations (each element can be increased at most once)
        # Since N is small (<=17), we can try all possibilities
        from itertools import product
        min_ops = float('inf')
        # Generate all possible combinations of operations (0 or 1 for each element)
        for ops in product([0, 1], repeat=N):
            new_R = [R[i] + ops[i] for i in range(N)]
            if is_possible(new_R):
                ops_count = sum(ops)
                if ops_count < min_ops:
                    min_ops = ops_count
        if min_ops != float('inf'):
            results.append(str(min_ops))
        else:
            results.append('-1')
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()