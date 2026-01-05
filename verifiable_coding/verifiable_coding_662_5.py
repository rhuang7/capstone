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
        group_size = count // d
        
        # First odd number in the range
        first_odd = L if L % 2 else L + 1
        # Last odd number in the range
        last_odd = R if R % 2 else R - 1
        
        # Sum of arithmetic sequence for each group
        # The first group is first_odd, first_odd + 2, ..., first_odd + 2*(group_size - 1)
        # The second group is first_odd + 2*group_size, first_odd + 2*group_size + 2, ..., first_odd + 2*group_size + 2*(group_size - 1)
        # And so on...
        
        total = 0
        for i in range(d):
            start = first_odd + 2 * i * group_size
            end = start + 2 * (group_size - 1)
            # Sum of arithmetic sequence: (first + last) * number_of_terms // 2
            num_terms = group_size
            sum_group = (start + end) * num_terms // 2
            total += sum_group
        
        results.append(total % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()