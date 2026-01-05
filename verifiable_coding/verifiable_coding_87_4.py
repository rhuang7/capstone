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
        
        # Calculate the number of ambiguous pairs
        # For each pair (x, y) with x < y, check if day x of month y and day y of month x are the same day of the week
        # The day of the week for day x of month y is (x - 1 + y * d) % w
        # The day of the week for day y of month x is (y - 1 + x * d) % w
        # We want these two to be equal
        
        # So, (x - 1 + y * d) % w == (y - 1 + x * d) % w
        # Simplify: (x - 1 + y * d) - (y - 1 + x * d) ≡ 0 mod w
        # => (x - 1 - y + 1 + y * d - x * d) ≡ 0 mod w
        # => (x - y + d(y - x)) ≡ 0 mod w
        # => (x - y)(1 - d) ≡ 0 mod w
        # => (x - y)(d - 1) ≡ 0 mod w
        
        # So, for (x, y) with x < y, we want (d - 1)(x - y) ≡ 0 mod w
        
        # Let's compute the number of pairs (x, y) with x < y and (d - 1)(x - y) ≡ 0 mod w
        
        # Let's denote k = d - 1
        k = d - 1
        
        # We need (k)(x - y) ≡ 0 mod w
        # Let's find the number of pairs (x, y) with x < y and k(x - y) ≡ 0 mod w
        
        # Let's find the number of pairs (x, y) with x < y and (x - y) ≡ 0 mod (w / gcd(k, w))
        
        from math import gcd
        
        g = gcd(k, w)
        w_div_g = w // g
        
        # The condition is (x - y) ≡ 0 mod (w_div_g)
        # So x ≡ y mod (w_div_g)
        
        # Now, we need to count the number of pairs (x, y) with x < y and x ≡ y mod (w_div_g)
        
        # Let's compute the number of such pairs
        
        # The number of valid (x, y) pairs is the sum for each residue r mod (w_div_g) of (count[r] choose 2)
        
        # But since x and y are in the range [1, m], we can compute for each residue r mod (w_div_g) the number of x in [1, m] with x ≡ r mod (w_div_g), then compute (count[r] choose 2)
        
        # However, since m and d can be up to 1e9, we need an efficient way to compute this
        
        # Let's compute for each residue r in 0..w_div_g-1:
        # count[r] = number of x in [1, m] with x ≡ r mod (w_div_g)
        
        # For each r in 0..w_div_g-1:
        # count[r] = floor((m - r) / w_div_g) + 1 if r <= m else 0
        
        # But since r ranges from 0 to w_div_g-1, and m can be up to 1e9, we can compute this efficiently
        
        # Now, we can compute the total number of pairs
        
        total = 0
        
        for r in range(w_div_g):
            # number of x in [1, m] with x ≡ r mod (w_div_g)
            if r == 0:
                count = m // w_div_g
            else:
                count = (m - r) // w_div_g + 1 if r <= m else 0
            total += count * (count - 1) // 2
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()