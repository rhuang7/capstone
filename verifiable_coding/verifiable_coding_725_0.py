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
        
        def is_safe(arr):
            for i in range(N - K + 1):
                sub = arr[i:i+K]
                max_val = max(sub)
                count = 0
                for j in range(K):
                    if sub[j] == max_val:
                        count += 1
                if count >= M:
                    return False
            return True
        
        from itertools import product
        min_ops = float('inf')
        for mask in product([0, 1], repeat=N):
            ops = sum(mask)
            if ops >= min_ops:
                continue
            new_R = [R[i] + mask[i] for i in range(N)]
            if is_safe(new_R):
                min_ops = ops
        if min_ops == float('inf'):
            results.append(-1)
        else:
            results.append(min_ops)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()