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
        # If all elements are the same and M <= K, it's impossible
        if all(r == R[0] for r in R):
            if M <= K:
                results.append(-1)
                continue
        
        # Try all possible ways to increase elements (each can be increased at most once)
        # Since N is small (<=17), we can try all possibilities
        from itertools import product
        
        min_ops = float('inf')
        # Try all combinations of increasing elements (0 or 1)
        for bits in product([0, 1], repeat=N):
            # Apply the operations
            new_R = [R[i] + bits[i] for i in range(N)]
            # Check if this new_R avoids arrest
            valid = True
            for i in range(N - K + 1):
                sub = new_R[i:i+K]
                max_val = max(sub)
                count = 0
                for j in range(K):
                    if sub[j] == max_val:
                        count += 1
                if count >= M:
                    valid = False
                    break
            if valid:
                ops = sum(bits)
                if ops < min_ops:
                    min_ops = ops
        results.append(min_ops if min_ops != float('inf') else -1)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()