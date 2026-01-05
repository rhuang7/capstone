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
        
        # Compute GCD of all elements
        gcd_all = A[0]
        for num in A[1:]:
            gcd_all = math.gcd(gcd_all, num)
            if gcd_all == 1:
                break  # GCD can't be less than 1
        
        if gcd_all == 1:
            results.append("-1")
        else:
            results.append(str(gcd_all))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()