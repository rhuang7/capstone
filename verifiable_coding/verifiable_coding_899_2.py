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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        max_candies = 0
        current = 0
        
        for i in range(N-1, -1, -1):
            current = max(A[i], current)
            max_candies = max(max_candies, current)
        
        results.append(str(max_candies))
    
    print('\n'.join(results))