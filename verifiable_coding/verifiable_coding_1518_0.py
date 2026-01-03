import sys
import math

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    max_n = 100000
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(max_n)) + 1):
        if is_prime[i]:
            for j in range(i*i, max_n + 1, i):
                is_prime[j] = False
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        
        if K == 1:
            if is_prime[N]:
                results.append('1')
            else:
                results.append('0')
            continue
        
        if N < K:
            results.append('0')
            continue
        
        if K == 2:
            if N >= 2 and is_prime[N - 2]:
                results.append('1')
            else:
                results.append('0')
            continue
        
        if K >= 3:
            if N >= 2 * K:
                results.append('1')
            else:
                results.append('0')
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()