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
        # Total numbers in range [n, m] is m - n + 1
        total = m - n + 1
        
        # Count numbers divisible by at least one of the values
        # Use inclusion-exclusion to calculate this
        # For 5 elements, the inclusion-exclusion formula is:
        # |A1 ∪ A2 ∪ A3 ∪ A4 ∪ A5| = Σ|Ai| - Σ|Ai ∩ Aj| + Σ|Ai ∩ Aj ∩ Ak| - ... + (-1)^{k+1} |A1 ∩ A2 ∩ ... ∩ Ak|}
        
        # We'll compute all subsets of the 5 values and calculate their intersections
        # For each subset, calculate the LCM of the values in the subset
        # Then count how many numbers in [n, m] are divisible by that LCM
        
        from itertools import combinations
        
        # Function to count numbers divisible by x in [n, m]
        def count_divisible(x):
            return (m // x) - ((n - 1) // x)
        
        # Inclusion-exclusion
        res = 0
        for i in range(1, 6):  # i is the size of the subset
            for subset in combinations(values, i):
                lcm = 1
                for num in subset:
                    lcm = lcm * num // (gcd(lcm, num))
                cnt = count_divisible(lcm)
                if i % 2 == 1:
                    res += cnt
                else:
                    res -= cnt
        
        # The answer is total - res
        print(total - res)
    
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    solve()