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
        M = int(data[idx+1])
        idx += 2
        
        matrix = []
        for _ in range(N):
            row = data[idx]
            matrix.append([int(c) for c in row])
            idx += 1
        
        collisions = 0
        for j in range(M):
            count = 0
            for i in range(N):
                if matrix[i][j] == 1:
                    count += 1
            if count >= 2:
                collisions += count * (count - 1) // 2
        
        results.append(str(collisions))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()