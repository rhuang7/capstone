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
        row_major = []
        for i in range(N):
            for j in range(M):
                row_major.append((i, j))
        
        col_major = []
        for j in range(M):
            for i in range(N):
                col_major.append((i, j))
        
        # For each K, compute the destroyed cells
        for K in range(total):
            destroyed_row = set()
            destroyed_col = set()
            
            # First hero (row-major)
            i = 0
            while i < total:
                if i % (K + 1) == 0:
                    destroyed_row.add(row_major[i])
                i += 1
            
            # Second hero (column-major)
            i = 0
            while i < total:
                if i % (K + 1) == 0:
                    destroyed_col.add(col_major[i])
                i += 1
            
            # Count cells destroyed by at least one hero
            count = len(destroyed_row.union(destroyed_col))
            res[K] = count
        
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))