import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        m = int(data[index+1])
        a = int(data[index+2])
        d = int(data[index+3])
        index += 4
        
        # Compute the 5 values: a, a+d, a+2d, a+3d, a+4d
        values = [a + i*d for i in range(5)]
        
        # Use inclusion-exclusion principle to count numbers not divisible by any of the values
        # Total numbers in range: m - n + 1
        total = m - n + 1
        
        # Count numbers divisible by at least one of the values
        # Using inclusion-exclusion for 5 sets
        # This is a simplified version for 5 values
        # For the actual implementation, we need to compute all combinations
        # But given the constraints, we can precompute all combinations of the 5 values
        # and apply inclusion-exclusion
        
        # Generate all non-empty subsets of the 5 values
        from itertools import combinations
        cnt = 0
        for k in range(1, 6):
            for subset in combinations(values, k):
                # Compute LCM of the subset
                lcm = subset[0]
                for num in subset[1:]:
                    lcm = lcm * num // (lcm // num)
                # Count numbers in [n, m] divisible by lcm
                count = (m // lcm) - ((n - 1) // lcm)
                if k % 2 == 1:
                    cnt += count
                else:
                    cnt -= count
        
        # The answer is total - cnt
        results.append(str(total - cnt))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()