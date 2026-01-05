import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, D = int(data[idx]), int(data[idx+1])
        idx += 2
        C = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Sort the cities by temperature
        C.sort()
        
        # Check if the first city is reachable from city 1
        if abs(C[0] - C[1]) > D:
            results.append("NO")
            continue
        
        # Check if the last city is reachable from the second last city
        if abs(C[-1] - C[-2]) > D:
            results.append("NO")
            continue
        
        # Check if all cities in the middle are reachable from their neighbors
        for i in range(1, N-1):
            if abs(C[i] - C[i-1]) > D or abs(C[i] - C[i+1]) > D:
                results.append("NO")
                break
        else:
            results.append("YES")
    
    print("\n".join(results))