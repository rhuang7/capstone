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
        idx += 1
        matrix = []
        for _ in range(N):
            row = list(map(int, data[idx:idx+N]))
            idx += N
            matrix.append(row)
        
        # Count the number of 1s in the matrix
        total_ones = sum(sum(row) for row in matrix)
        
        # The minimum possible bandwidth is 0 if there are no 1s
        if total_ones == 0:
            results.append(0)
            continue
        
        # The maximum possible bandwidth is N-1
        # We want to find the smallest K such that we can place all 1s within K diagonal bands
        # The number of positions available in each band is 2K + 1 (for K=0, it's 1; for K=1, it's 3, etc.)
        # We need to find the smallest K such that (2K + 1) * K >= total_ones
        
        K = 0
        while (2*K + 1) * K < total_ones:
            K += 1
        
        results.append(K)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()