import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        K = int(data[i])
        pattern = []
        
        for j in range(1, K + 1):
            pattern.append(str(j))
        pattern.append('1')
        results.append(''.join(pattern))
        
        for j in range(K - 1, 0, -1):
            pattern = []
            for k in range(1, j + 1):
                pattern.append(str(k))
            pattern.append('1')
            results.append(''.join(pattern))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()