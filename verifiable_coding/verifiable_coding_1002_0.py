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
        
        # Sort the temperatures
        C.sort()
        
        # Check if the first city can reach the second, third, etc.
        # We need to check if the maximum difference between consecutive cities is <= D
        # But since we can choose any path, we need to check if the first city can reach all others through some path
        # However, since the graph is undirected and connected if all cities are within D of each other, we can check if the max difference between any two cities is <= D
        # But since Chef starts at city 1, we need to check if city 1 can reach all others through some path
        # The key insight is that if the temperature of city 1 is within D of the temperature of city N, then there exists a path
        # Because the cities are sorted, the max difference between any two cities is C[-1] - C[0]
        # So if C[-1] - C[0] <= D, then all cities are within D of each other, and Chef can visit all cities
        # But since Chef starts at city 1, we need to check if city 1 can reach all others
        # However, if the max difference between any two cities is <= D, then there exists a path
        # So the answer is YES if the max difference between any two cities is <= D
        # But since Chef starts at city 1, we need to check if city 1 can reach all others
        # The maximum difference between any two cities is C[-1] - C[0]
        # So if C[-1] - C[0] <= D, then YES, else NO
        
        if C[-1] - C[0] <= D:
            results.append("YES")
        else:
            results.append("NO")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()