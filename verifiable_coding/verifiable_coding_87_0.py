import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        m = int(data[index])
        d = int(data[index+1])
        w = int(data[index+2])
        index += 3
        
        # Calculate the total number of days in the year
        total_days = m * d
        
        # Calculate the number of days in the week
        week_days = w
        
        # Calculate the number of ambiguous pairs
        # For each pair (x, y) where x < y, check if day x of month y and day y of month x are the same day of the week
        # The day of the week for day x of month y is (x - 1 + y * d) % w
        # The day of the week for day y of month x is (y - 1 + x * d) % w
        # We want these two to be equal
        
        # Let's find all pairs (x, y) with x < y such that (x - 1 + y * d) % w == (y - 1 + x * d) % w
        
        # Simplify the equation:
        # (x - 1 + y * d) % w == (y - 1 + x * d) % w
        # (x - 1 + y * d) - (y - 1 + x * d) ≡ 0 mod w
        # (x - 1 - y + 1 + y * d - x * d) ≡ 0 mod w
        # (x - y + d(y - x)) ≡ 0 mod w
        # (x - y)(1 - d) ≡ 0 mod w
        # (x - y)(d - 1) ≡ 0 mod w
        
        # So, for (x, y) to be ambiguous, (x - y)(d - 1) must be divisible by w
        
        # Let's find all pairs (x, y) with x < y and (x - y)(d - 1) ≡ 0 mod w
        
        # Let's find all possible values of (x - y) that satisfy this condition
        
        # Let's denote k = x - y
        # Then k * (d - 1) ≡ 0 mod w
        # So k must be a multiple of w / gcd(w, d - 1)
        
        # Let's compute the gcd
        from math import gcd
        g = gcd(w, d - 1)
        divisor = w // g
        
        # Now, find all k such that k is a multiple of divisor and k < 0 (since x < y)
        # Because k = x - y < 0
        
        # Let's find all possible k values
        # k must be a negative multiple of divisor
        # Let's find the maximum absolute value of k such that x and y are within the valid ranges
        
        # x can be from 1 to d
        # y can be from 1 to m
        
        # So x < y => y > x
        # So k = x - y < 0
        
        # Let's find all possible k values
        # k must be a multiple of divisor
        # Let's find the maximum possible |k| such that x and y are valid
        
        # Let's find the maximum possible |k| such that x and y are valid
        # Since x can be at most d and y can be at most m, the maximum |k| is d - 1 (when x = 1, y = d)
        # But since k must be negative, the maximum |k| is min(d - 1, m - 1)
        
        max_k_abs = min(d - 1, m - 1)
        
        # Now, find all multiples of divisor that are negative and have absolute value <= max_k_abs
        # The number of such k is floor(max_k_abs / divisor)
        
        count = 0
        for k in range(-max_k_abs, 0):
            if k % divisor == 0:
                count += 1
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()