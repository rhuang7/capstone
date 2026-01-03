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
        # For each pair (x, y) with x < y, check if day x of month y and day y of month x are same day of week
        # Total days in year = m * d
        total_days = m * d
        
        # The day of the week for day x of month y is (x - 1 + y * d) % w
        # The day of the week for day y of month x is (y - 1 + x * d) % w
        # We want these two to be equal
        
        # So (x - 1 + y * d) % w == (y - 1 + x * d) % w
        # Which simplifies to (x - 1 + y * d) - (y - 1 + x * d) ≡ 0 mod w
        # => (x - 1 - y + 1 + y * d - x * d) ≡ 0 mod w
        # => (x - y + d(y - x)) ≡ 0 mod w
        # => (x - y)(1 - d) ≡ 0 mod w
        # => (x - y)(d - 1) ≡ 0 mod w
        
        # So for (x, y) to be ambiguous, (x - y)(d - 1) must be divisible by w
        
        # Let's find the number of pairs (x, y) with x < y such that (x - y)(d - 1) ≡ 0 mod w
        
        # Let's compute the number of such pairs
        # Let's denote k = d - 1
        k = d - 1
        
        # We need (x - y) * k ≡ 0 mod w
        # Let's find all (x, y) with x < y and (x - y) * k ≡ 0 mod w
        
        # Let's find all possible (x - y) values such that (x - y) * k ≡ 0 mod w
        # Let's denote delta = x - y
        # So delta * k ≡ 0 mod w
        # => delta ≡ 0 mod (w / gcd(k, w))
        
        gcd_k_w = (k * w) // (k // (k % w) if k % w != 0 else w)
        mod = w // gcd_k_w
        
        # Now find all delta such that delta ≡ 0 mod mod
        # delta can be from - (y - 1) to (x - 1), but since x < y, delta is negative
        
        # The number of such delta is equal to the number of pairs (x, y) with x < y and delta ≡ 0 mod mod
        
        # For each possible delta (negative), count the number of (x, y) pairs with x - y = delta
        
        # Let's find all possible delta values
        # delta can be from - (d - 1) to -1 (since x < y, delta is negative)
        
        # We need to find the number of (x, y) pairs with x < y and x - y ≡ 0 mod mod
        
        # Let's compute the number of such pairs
        count = 0
        for delta in range(-1, -d, -1):
            if delta % mod == 0:
                # For this delta, how many (x, y) pairs have x - y = delta
                # x = y + delta
                # y must be >= 1, x must be <= d
                # So y can range from 1 to (d - delta)
                # But also, x must be <= d
                # So y can range from 1 to (d - delta)
                # But since x < y, delta is negative, so y must be >= 1, x = y + delta must be >= 1
                # So y >= max(1, -delta + 1)
                # And x = y + delta must be <= d
                # So y <= d - delta
                # So the number of valid y is max(0, d - delta - max(1, -delta + 1) + 1)
                # But since delta is negative, let's rewrite it
                # delta = -k, where k > 0
                # x = y - k
                # y must be >= k + 1
                # x must be <= d
                # So y can range from k + 1 to d
                # Number of valid y is d - (k + 1) + 1 = d - k
                # But k = -delta
                # So number of valid y is d - (-delta)
                # So for each valid delta, the number of valid (x, y) pairs is d - (-delta)
                # But delta must be negative
                # So delta = -k, where k > 0
                # So number of valid (x, y) pairs is d - k
                # But k must be such that delta is divisible by mod
                # So for each delta, we can compute k = -delta
                # And check if k is such that delta is divisible by mod
                # So for each delta, if delta % mod == 0, then we can compute the number of valid (x, y) pairs
                # So the number of valid (x, y) pairs is d - k
                # But k = -delta
                # So the number of valid (x, y) pairs is d - (-delta)
                # So the number of valid (x, y) pairs is d + delta
                # But delta is negative, so this is d - |delta|
                # But delta must be divisible by mod
                # So for each delta, if delta is divisible by mod, then the number of valid (x, y) pairs is d + delta
                # But we need to make sure that x = y + delta is <= d
                # So y must be >= 1, and x = y + delta must be <= d
                # So y can range from 1 to d - delta
                # So the number of valid (x, y) pairs is max(0, d - delta - 1 + 1) = max(0, d - delta)
                # But delta is negative, so d - delta is positive
                # So the number of valid (x, y) pairs is d - delta
                # So for each valid delta, add d - delta to the count
                count += d - delta
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()