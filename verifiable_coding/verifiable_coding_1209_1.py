import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    n = int(data[0])
    idx = 1
    results = []
    
    for _ in range(n):
        v1 = int(data[idx])
        t1 = int(data[idx+1])
        v2 = int(data[idx+2])
        t2 = int(data[idx+3])
        v3 = int(data[idx+4])
        t3 = int(data[idx+5])
        idx += 6
        
        # Check if it's possible to get exactly t3 temperature with at least v3 volume
        # The temperature of the mixture is (v1*t1 + v2*t2) / (v1 + v2)
        # We need (v1*t1 + v2*t2) / (v1 + v2) = t3 and v1 + v2 >= v3
        
        # Check if t3 is between t1 and t2 (inclusive)
        if t3 < t1 or t3 > t2:
            results.append("NO")
            continue
        
        # Check if there exists a combination of v1' and v2' such that:
        # v1' + v2' >= v3 and (v1'*t1 + v2'*t2) / (v1' + v2') = t3
        # This is equivalent to v1'*t1 + v2'*t2 = t3*(v1' + v2')
        # => v1'(t1 - t3) + v2'(t2 - t3) = 0
        
        # Let's find the minimum and maximum possible volumes of water that can be mixed
        # to get temperature t3
        # Let x be the volume of cold water, y be the volume of hot water
        # x + y >= v3
        # x*(t1 - t3) + y*(t2 - t3) = 0
        
        # Since t3 is between t1 and t2, t1 - t3 is negative and t2 - t3 is positive
        # So we can solve for y in terms of x: y = x*(t3 - t1)/(t2 - t3)
        # We need x >= 0, y >= 0, and x + y >= v3
        
        # Let's find the minimum x such that y >= 0 and x + y >= v3
        # y = x*(t3 - t1)/(t2 - t3)
        # x + y = x + x*(t3 - t1)/(t2 - t3) = x*(1 + (t3 - t1)/(t2 - t3)) = x*( (t2 - t3) + t3 - t1 ) / (t2 - t3)
        # = x*(t2 - t1) / (t2 - t3)
        # We need x*(t2 - t1) / (t2 - t3) >= v3
        # => x >= v3 * (t2 - t3) / (t2 - t1)
        
        # Also, since y = x*(t3 - t1)/(t2 - t3), we need y >= 0 => x >= 0
        
        # So the minimum x is max(0, v3 * (t2 - t3) / (t2 - t1))
        
        # Now check if there exists x and y such that x + y >= v3 and x*(t1 - t3) + y*(t2 - t3) = 0
        
        # We can use binary search or check if there's a solution in the range of possible x and y
        
        # Since t3 is between t1 and t2, there is a solution if and only if:
        # (v1 + v2) >= v3 and (v1*t1 + v2*t2) / (v1 + v2) == t3
        
        # But we can't just use v1 and v2 because we can take any amount from each bucket
        
        # So we need to find if there exists x and y such that:
        # x + y >= v3
        # x*(t1 - t3) + y*(t2 - t3) = 0
        
        # Let's find the minimum x such that y >= 0 and x + y >= v3
        # y = x*(t3 - t1)/(t2 - t3)
        # x + y = x + x*(t3 - t1)/(t2 - t3) = x*( (t2 - t3) + t3 - t1 ) / (t2 - t3)
        # = x*(t2 - t1) / (t2 - t3)
        # We need x*(t2 - t1) / (t2 - t3) >= v3
        # => x >= v3 * (t2 - t3) / (t2 - t1)
        
        # So the minimum x is max(0, v3 * (t2 - t3) / (t2 - t1))
        
        # Now check if there's a possible x and y that satisfy the conditions
        
        # Let's try x = 0, then y = v3
        # Check if y*(t2 - t3) = 0 => t2 - t3 = 0 => t2 = t3
        # But t3 is between t1 and t2, so t2 - t3 can't be zero unless t3 = t2
        
        # So we can try x = 0 and y = v3, and check if it gives t3
        # Similarly, try y = 0 and x = v3
        
        # Check if using only cold water gives t3
        if t1 == t3 and v1 >= v3:
            results.append("YES")
            continue
        
        # Check if using only hot water gives t3
        if t2 == t3 and v2 >= v3:
            results.append("YES")
            continue
        
        # Check if there's a way to mix some cold and some hot water to get t3
        # We can use the formula for the temperature of the mixture
        # t3 = (x*t1 + y*t2) / (x + y)
        # We need x + y >= v3 and x*t1 + y*t2 = t3*(x + y)
        
        # Let's try to find x and y such that x + y >= v3 and x*t1 + y*t2 = t3*(x + y)
        
        # We can use binary search or check if there's a solution in the range of possible x and y
        
        # Let's try to find the minimum x such that y = (t3 - t1) * x / (t2 - t1)
        # and x + y >= v3
        
        # Let's compute the minimum x that satisfies this
        
        min_x = 0
        if t2 - t1 > 0:
            min_x = (v3 * (t2 - t3)) / (t2 - t1)
        
        # Now check if there's a possible x and y in the range of v1 and v2
        # We can try x = max(0, min_x) and y = (t3 - t1) * x / (t2 - t1)
        # and check if x <= v1 and y <= v2 and x + y >= v3
        
        # Try x = max(0, min_x)
        x = max(0, min_x)
        y = (t3 - t1) * x / (t2 - t1)
        
        if x <= v1 and y <= v2 and x + y >= v3:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()