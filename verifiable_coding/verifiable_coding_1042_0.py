import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        P = int(data[index+1])
        index += 2
        
        # Find all numbers from 1 to N that are coprime with P
        coprimes = []
        for i in range(1, N+1):
            if math.gcd(i, P) == 1:
                coprimes.append(i)
        
        # Count pairs (a, b) where a < b and both are coprimes with P
        count = 0
        m = len(coprimes)
        for i in range(m):
            for j in range(i+1, m):
                count += 1
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()