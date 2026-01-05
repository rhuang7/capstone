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
        
        for i in range(n):
            current_gcd = A[i]
            for j in range(i + 1, n):
                current_gcd = math.gcd(current_gcd, A[j])
                if current_gcd == 1:
                    max_len = max(max_len, j - i + 1)
        
        results.append(str(max_len) if max_len != -1 else "-1")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()