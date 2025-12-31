import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    
    results = []
    
    for _ in range(t):
        m = int(data[idx])
        d = int(data[idx+1])
        w = int(data[idx+2])
        idx += 3
        
        # Calculate the total number of days in the year
        total_days = m * d
        
        # Calculate the number of days in the week
        week_days = w
        
        # Calculate the number of ambiguous pairs
        # For each pair (x, y) with x < y, check if day x of month y and day y of month x are same day of the week
        # The day of the week for day x of month y is (x + (y-1)*d) % w
        # The day of the week for day y of month x is (y + (x-1)*d) % w
        # We need (x + (y-1)*d) % w == (y + (x-1)*d) % w
        
        # Simplify the equation:
        # (x + (y-1)*d) % w == (y + (x-1)*d) % w
        # => (x + y*d - d) % w == (y + x*d - d) % w
        # => (x + y*d - d - y - x*d + d) % w == 0
        # => (x - y + y*d - x*d) % w == 0
        # => (x(1 - d) + y(d - 1)) % w == 0
        # => (x - y)(1 - d) % w == 0
        # => (x - y)(d - 1) % w == 0
        
        # So, for each pair (x, y) with x < y, we need (x - y)(d - 1) % w == 0
        
        # Let's compute the number of such pairs
        # Let's denote k = d - 1
        k = d - 1
        
        # We need (x - y) * k % w == 0
        # Let's find the number of pairs (x, y) with x < y and (x - y) * k % w == 0
        
        # Let's consider all possible values of (x - y) mod w
        # For each possible value of (x - y) mod w, we need (value * k) % w == 0
        
        # Let's find all values of r in [0, w-1] such that (r * k) % w == 0
        valid_r = []
        for r in range(w):
            if (r * k) % w == 0:
                valid_r.append(r)
        
        # Now, for each valid r, count the number of pairs (x, y) with x < y and (x - y) mod w == r
        # Note that r can be 0, but in that case, x = y, which is not allowed (x < y)
        # So we exclude r = 0
        
        valid_r = [r for r in valid_r if r != 0]
        
        # Now, for each valid r, count the number of pairs (x, y) with x < y and (x - y) mod w == r
        
        # Let's compute the total number of such pairs
        total = 0
        
        # For each valid r, the number of pairs (x, y) with x < y and (x - y) mod w == r is equal to
        # the number of pairs (x, y) such that y = x - r mod w, and x < y
        
        # Let's find the number of pairs (x, y) with x < y and (x - y) mod w == r
        # This is equivalent to finding the number of pairs (x, y) such that y = x - r mod w and x < y
        
        # Let's iterate over all possible values of x and y
        # Since m and d are up to 1e9, we need an efficient way to compute this
        
        # The number of pairs (x, y) with x < y and (x - y) mod w == r is equal to
        # the number of pairs (x, y) such that y = x - r mod w and x < y
        
        # Since r is fixed, we can compute the number of such pairs as follows:
        # For each possible value of x, y = x - r mod w
        # If y > x, then it's a valid pair
        
        # But since x and y can be up to m * d, which is up to 1e18, we can't iterate over all x
        
        # Instead, we can find the number of pairs (x, y) with x < y and (x - y) mod w == r
        # This is equivalent to the number of pairs (x, y) such that y = x - r mod w and x < y
        
        # Let's compute the number of such pairs for each valid r
        
        for r in valid_r:
            # We need to find the number of pairs (x, y) with x < y and (x - y) mod w == r
            # This is equivalent to y = x - r mod w, and x < y
            
            # Let's find the number of such pairs
            # We can think of it as the number of pairs (x, y) such that y = x - r mod w and x < y
            
            # Let's compute the number of such pairs
            # For each possible x, y = x - r mod w
            # If y > x, then it's a valid pair
            
            # Let's find the number of x such that y > x
            # y = x - r mod w
            # So, y = x - r + k * w for some integer k
            # We want y > x
            # So, x - r + k * w > x
            # => -r + k * w > 0
            # => k * w > r
            # => k > r / w
            # Since r < w, r / w < 1, so k >= 1
            
            # So, for each x, we can find the number of k such that y = x - r + k * w > x
            
            # The number of such k is floor((total_days - x + r) / w)
            # But since x can be up to total_days, we need to find the number of x such that y > x
            
            # Let's find the number of x such that y > x
            # y = x - r + k * w
            # y > x => -r + k * w > 0 => k > r / w
            # Since r < w, r / w < 1, so k >= 1
            
            # So, for each x, there is exactly one k (k=1) that satisfies this condition
            # So, for each x, we have one y such that y = x - r + w
            # We need to check if y <= total_days
            
            # So, the number of such pairs is the number of x such that y = x - r + w <= total_days and x < y
            
            # y = x - r + w
            # x < y => x < x - r + w => 0 < -r + w => w > r, which is always true since r < w
            
            # So, the number of such pairs is the number of x such that y = x - r + w <= total_days
            
            # y = x - r + w <= total_days
            # => x <= total_days + r - w
            # Since x >= 1, the number of such x is max(0, total_days + r - w - 1 + 1)
            # => max(0, total_days + r - w)
            
            count = max(0, total_days + r - w)
            total += count
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()