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
        
        # The sequence is first_odd, first_odd + 2, ..., last_odd
        # We need to take every d-th odd number, starting from the first
        # So the first term is first_odd, the second is first_odd + 2*d, etc.
        
        # Number of terms to take is total_terms
        # The sum of an arithmetic sequence is (n * (a1 + an)) // 2
        a1 = first_odd
        an = first_odd + 2 * (total_terms - 1) * d
        sum_seq = (total_terms * (a1 + an)) // 2
        results.append(sum_seq % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()