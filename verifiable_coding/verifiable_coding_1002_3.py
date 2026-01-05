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
        
        # Check if the first city can reach the last city with the given D
        if abs(C[0] - C[-1]) > D:
            results.append("NO")
            continue
        
        # Check if there's a way to connect all cities in a path
        # We can use a greedy approach: check if each city is within D of the previous one
        # But since the cities are sorted, we can check if the max difference between consecutive cities is <= D
        max_diff = 0
        for i in range(1, N):
            diff = abs(C[i] - C[i-1])
            if diff > max_diff:
                max_diff = diff
        if max_diff <= D:
            results.append("YES")
        else:
            results.append("NO")
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()