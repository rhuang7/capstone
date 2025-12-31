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
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        max_len = -1
        n = len(A)
        
        # Track the current GCD for each position
        current_gcd = A[0]
        for i in range(1, n):
            current_gcd = math.gcd(current_gcd, A[i])
            if current_gcd == 1:
                max_len = max(max_len, i + 1)
        
        if max_len == -1:
            results.append("-1")
        else:
            results.append(str(max_len))
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()