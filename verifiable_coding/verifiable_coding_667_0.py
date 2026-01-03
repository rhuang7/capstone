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
        N, D = int(data[idx]), int(data[idx+1])
        idx += 2
        X = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Compute the latest day for each route
        latest = [0] * N
        for i in range(N):
            # The latest day for the i-th route is the largest multiple of X[i] <= D
            latest[i] = (D // X[i]) * X[i]
        
        # Find the minimum latest day across all routes
        Y = min(latest)
        results.append(Y)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()