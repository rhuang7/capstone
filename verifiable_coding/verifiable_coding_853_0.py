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
        
        drivers = []
        
        for _ in range(N):
            name = data[idx]
            time = int(data[idx + 1])
            drivers.append((time, name))
            idx += 2
        
        # Sort drivers by time in ascending order
        drivers.sort()
        
        # Extract names in order
        for time, name in drivers:
            results.append(name)
    
    for name in results:
        print(name)

if __name__ == '__main__':
    solve()