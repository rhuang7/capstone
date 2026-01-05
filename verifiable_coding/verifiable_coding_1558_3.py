import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        
        total = N * M
        res = [0] * total
        
        # Precompute positions for row-major and column-major order
        row_major = [(i, j) for i in range(N) for j in range(M)]
        col_major = [(i, j) for j in range(M) for i in range(N)]
        
        # For each K, compute the number of destroyed cells
        for K in range(total):
            destroyed = set()
            
            # First hero (row-major)
            for i in range(total):
                if i % (K + 1) == 0:
                    destroyed.add(row_major[i])
            
            # Second hero (column-major)
            for i in range(total):
                if i % (K + 1) == 0:
                    destroyed.add(col_major[i])
            
            res[K] = len(destroyed)
        
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()