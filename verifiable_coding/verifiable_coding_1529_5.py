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
        L = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Calculate the sum of all permutations
        # Each digit contributes to each position in the number
        # For each position i (0-based), each digit appears (N-1)! times
        # So total contribution of a digit d at position i is d * 10^i * (N-1)!
        factorial = [1] * (N + 1)
        for i in range(1, N + 1):
            factorial[i] = factorial[i - 1] * i
        
        total = 0
        for i in range(N):
            count = factorial[N - 1]
            for d in L:
                total += d * count * (10 ** i)
        
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()