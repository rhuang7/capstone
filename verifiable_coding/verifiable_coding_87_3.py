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
        # Day of week for day x of month y: (x - 1 + y * d) % w
        # Day of week for day y of month x: (y - 1 + x * d) % w
        # We need (x - 1 + y * d) % w == (y - 1 + x * d) % w
        # Simplify: (x - 1 + y * d) ≡ (y - 1 + x * d) mod w
        # => x - 1 + y * d ≡ y - 1 + x * d mod w
        # => x - 1 - y + 1 ≡ x * d - y * d mod w
        # => x - y ≡ d(x - y) mod w
        # => (x - y)(1 - d) ≡ 0 mod w
        # => (x - y)(d - 1) ≡ 0 mod w
        # So, (x - y) must be a multiple of w / gcd(d - 1, w)
        # Let g = gcd(d - 1, w)
        # Then, (x - y) must be a multiple of w / g
        # Let k = w / g
        # So, x - y = k * t for some integer t
        # But x < y, so x - y is negative, so t must be negative
        # So, y - x = k * |t|
        # Let's find the number of pairs (x, y) with x < y and y - x is a multiple of k
        # The number of such pairs is equal to the number of pairs (x, y) with 1 <= x < y <= m * d and y - x is a multiple of k
        
        # Compute g = gcd(d - 1, w)
        g = 1
        for i in range(2, min(d - 1, w) + 1):
            if d - 1 % i == 0 and w % i == 0:
                g = i
        k = w // g
        
        # Now, find the number of pairs (x, y) with 1 <= x < y <= total_days and y - x is a multiple of k
        # Let's iterate over all possible values of y - x = k * t, t >= 1
        # For each t, the number of pairs is (total_days - k * t) // k
        # Sum over all t such that k * t <= total_days - 1
        count = 0
        max_t = (total_days - 1) // k
        for t in range(1, max_t + 1):
            count += (total_days - k * t) // k
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()