import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
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
        # We'll compute the count of numbers divisible by each value, their pairwise intersections, etc.
        # But since the values can be large, we'll use the inclusion-exclusion formula for 5 sets
        
        # For simplicity, we'll use a set to store the values and then compute the inclusion-exclusion
        # But since the values can be large, we'll need to handle them carefully
        
        # Create a set of the values
        s = set(values)
        
        # Use inclusion-exclusion to count numbers divisible by at least one of the values
        # This is a simplified version for 5 values
        # We'll compute the count of numbers divisible by each value, then subtract the pairwise intersections, add the triple intersections, etc.
        
        # Count of numbers divisible by a value x in [n, m]
        def count_divisible(x):
            return (m // x) - ((n - 1) // x)
        
        # Inclusion-exclusion for 5 sets
        # We'll generate all possible non-empty subsets of the 5 values
        # For each subset, compute the LCM of the elements and the size of the subset
        # If the size is odd, add the count, else subtract
        
        from itertools import combinations
        
        res = 0
        for k in range(1, 6):
            for subset in combinations(s, k):
                # Compute LCM of the subset
                lcm = subset[0]
                for num in subset[1:]:
                    lcm = lcm * num // (lcm // num)
                # Count numbers divisible by lcm in [n, m]
                cnt = count_divisible(lcm)
                # If k is odd, add, else subtract
                if k % 2 == 1:
                    res += cnt
                else:
                    res -= cnt
        
        # The answer is total - res
        print(total - res)

if __name__ == '__main__':
    solve()