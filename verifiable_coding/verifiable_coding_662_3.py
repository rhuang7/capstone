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
        
        # Count number of odd numbers between L and R
        count = ((R + 1) // 2) - (L // 2)
        
        # Total numbers to take is count // d * d
        total = count // d * d
        
        # First odd number in range
        first = L if L % 2 else L + 1
        # Last odd number in range
        last = R if R % 2 else R - 1
        
        # Number of terms in the sequence
        n = total // d
        
        # Sum of arithmetic sequence: n/2 * (2a + (n-1)d)
        a = first
        common_diff = 2 * d
        sum_seq = (n * (2 * a + (n - 1) * common_diff)) // 2
        
        results.append(sum_seq % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()