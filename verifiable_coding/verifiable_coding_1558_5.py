import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        M = int(data[index + 1])
        index += 2
        
        total = N * M
        output = [0] * total
        
        # Precompute positions for row-major and column-major order
        row_major = [(i, j) for i in range(N) for j in range(M)]
        col_major = [(i, j) for j in range(M) for i in range(N)]
        
        # For each K, compute the number of destroyed cells
        for K in range(total):
            destroyed = set()
            
            # First hero (row-major)
            i = 0
            while i < total:
                if i % (K + 1) == 0:
                    destroyed.add(row_major[i])
                i += 1
            
            # Second hero (column-major)
            i = 0
            while i < total:
                if i % (K + 1) == 0:
                    destroyed.add(col_major[i])
                i += 1
            
            output[K] = len(destroyed)
        
        results.append(' '.join(map(str, output)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()