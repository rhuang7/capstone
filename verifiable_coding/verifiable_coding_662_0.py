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
        
        # The sequence of odd numbers is an arithmetic progression with common difference 2
        # We need to select every d-th odd number, starting from the first
        # So the selected numbers are first_odd, first_odd + 2*d, first_odd + 4*d, ...
        
        # The sum of an arithmetic progression is (n * (a1 + an)) // 2
        # Here, a1 is first_odd, an is first_odd + 2*(d-1)*d, n is total_terms
        a1 = first_odd
        an = a1 + 2 * (d - 1) * d
        n = total_terms
        sum_ap = (n * (a1 + an)) // 2
        
        results.append(sum_ap % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()