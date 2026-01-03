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
        speeds = list(map(int, data[idx:idx + N + 1]))
        idx += N + 1
        
        S0 = speeds[0]
        count = 0
        
        for i in range(1, N + 1):
            if speeds[i] > S0:
                count += 1
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()