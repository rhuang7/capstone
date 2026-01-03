import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        N = int(data[index])
        M = int(data[index+1])
        index += 2
        
        total = N * M
        result = [0] * total
        
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
            for i in range(total):
                if i % (K + 1) == 0:
                    destroyed_row.add(row_major[i])
            
            # Second hero (column-major)
            for i in range(total):
                if i % (K + 1) == 0:
                    destroyed_col.add(col_major[i])
            
            # Count cells destroyed by at least one hero
            count = len(destroyed_row.union(destroyed_col))
            result[K] = count
        
        # Print the result for this test case
        print(' '.join(map(str, result)))

if __name__ == '__main__':
    solve()