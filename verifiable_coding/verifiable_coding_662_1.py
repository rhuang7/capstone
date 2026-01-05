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
        
        # The sum of alternate d odd numbers can be calculated as:
        # For each group of d odd numbers, take the first, second, ..., d-th
        # Then repeat this for all groups
        # This is equivalent to taking every (d + 1)-th odd number starting from first_odd
        # So the sequence is first_odd, first_odd + (d + 1), first_odd + 2*(d + 1), ...
        # Number of terms is total_terms
        
        # Sum of arithmetic sequence: n/2 * (2a + (n-1)*d)
        a = first_odd
        n = total_terms
        d_seq = (d + 1)
        sum_seq = n * (2 * a + (n - 1) * d_seq) // 2
        results.append(sum_seq % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()