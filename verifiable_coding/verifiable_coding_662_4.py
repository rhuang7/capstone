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
        # Since count is a multiple of d, we can safely divide
        total_terms = count // d
        
        # First odd number in the range
        first_odd = L if L % 2 else L + 1
        # Last odd number in the range
        last_odd = R if R % 2 else R - 1
        
        # The sum of alternate d odd numbers is the sum of every d-th odd number
        # Starting from first_odd, take every d-th odd number for total_terms times
        # The sequence is first_odd, first_odd + 2*d, first_odd + 4*d, ...
        # This is an arithmetic sequence with a = first_odd, d = 2*d, n = total_terms
        
        a = first_odd
        diff = 2 * d
        n = total_terms
        
        # Sum of arithmetic sequence: n/2 * (2a + (n-1)*diff)
        sum_seq = (n * (2 * a + (n - 1) * diff)) // 2
        
        results.append(sum_seq % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()