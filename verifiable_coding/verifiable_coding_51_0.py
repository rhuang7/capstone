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
        k = int(data[index+1])
        d1 = int(data[index+2])
        d2 = int(data[index+3])
        index += 4
        
        # Total wins after all games must be n
        # Let a, b, c be the number of wins of each team
        # a + b + c = n
        # |a - b| = d1
        # |b - c| = d2
        # Also, a, b, c >= 0
        
        # Since all teams must have equal number of wins, a = b = c = n // 3
        # But n must be divisible by 3
        if n % 3 != 0:
            results.append("no")
            continue
        
        total = n // 3
        # The current wins of the teams must be such that they can reach total
        # Let current wins be a, b, c
        # a + b + c = k
        # |a - b| = d1
        # |b - c| = d2
        # a, b, c >= 0
        
        # We need to check if there exists a, b, c such that:
        # a + b + c = k
        # |a - b| = d1
        # |b - c| = d2
        # a, b, c >= 0
        # and after adding (n - k) games, a, b, c all become total
        
        # The total wins for each team after all games is total
        # So, the current wins must be such that:
        # a = total - x
        # b = total - y
        # c = total - z
        # where x + y + z = n - k
        # and x, y, z >= 0
        # Also, |a - b| = d1 => |x - y| = d1
        # |b - c| = d2 => |y - z| = d2
        
        # Let's try all possible combinations of x, y, z that satisfy the conditions
        
        # We can try all possible combinations of x, y, z that satisfy the conditions
        # and check if x + y + z = n - k and x, y, z >= 0
        
        # Let's try all possible values for x, y, z that satisfy the conditions
        # Since n can be up to 1e12, we need an efficient way to check
        # We can use the fact that the difference between a and b is d1, and between b and c is d2
        # So, a = b + d1 or a = b - d1
        # c = b + d2 or c = b - d2
        
        # We can try all 4 combinations of signs
        found = False
        for sign1 in [-1, 1]:
            for sign2 in [-1, 1]:
                a = total + sign1 * d1
                c = total + sign2 * d2
                b = total
                # Check if a + b + c = k
                if a + b + c == k:
                    found = True
                    break
                # Try other combinations
                a = total - sign1 * d1
                c = total - sign2 * d2
                b = total
                if a + b + c == k:
                    found = True
                    break
                # Try a = b + d1, c = b - d2
                a = total + d1
                c = total - d2
                b = total
                if a + b + c == k:
                    found = True
                    break
                # Try a = b - d1, c = b + d2
                a = total - d1
                c = total + d2
                b = total
                if a + b + c == k:
                    found = True
                    break
            if found:
                break
        
        results.append("yes" if found else "no")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()