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
        
        # Check if the first city can reach the second, third, etc.
        # Since the cities are sorted, we only need to check the first and last city
        # because if the first can reach the last, then all in between can be connected
        # in some order
        if abs(C[0] - C[-1]) <= D:
            results.append("YES")
        else:
            results.append("NO")
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()