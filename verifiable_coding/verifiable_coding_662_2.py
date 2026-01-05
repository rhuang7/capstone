import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    
    for _ in range(T):
        d = int(data[idx])
        idx += 1
        L = int(data[idx])
        R = int(data[idx + 1])
        idx += 2
        
        # Count the number of odd numbers between L and R
        count = ((R + 1) // 2) - (L // 2)
        # Since count is a multiple of d, we can safely divide
        total = count // d
        
        # First odd number in the range
        first = L if L % 2 else L + 1
        # Last odd number in the range
        last = R if R % 2 else R - 1
        
        # Sum of arithmetic sequence
        sum_odd = (total * (first + (first + 2 * (total - 1)))) // 2
        
        # Multiply by d (since we take d alternate numbers)
        result = (sum_odd * d) % MOD
        results.append(result)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()