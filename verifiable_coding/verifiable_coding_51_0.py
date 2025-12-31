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
        
        # Total wins needed for each team
        total = n
        
        # Let x, y, z be the number of wins of teams 1, 2, 3
        # x - y = d1, y - z = d2
        # x + y + z = total
        # Also, x, y, z must be non-negative integers
        
        # From the equations:
        # x = y + d1
        # z = y - d2
        # Substituting into x + y + z = total:
        # (y + d1) + y + (y - d2) = total
        # 3y + d1 - d2 = total
        # y = (total - d1 + d2) / 3
        
        # Check if (total - d1 + d2) is divisible by 3
        if (total - d1 + d2) % 3 != 0:
            results.append("no")
            continue
        
        y = (total - d1 + d2) // 3
        x = y + d1
        z = y - d2
        
        # Check if x, y, z are non-negative and their sum is total
        if x < 0 or y < 0 or z < 0 or x + y + z != total:
            results.append("no")
            continue
        
        # Check if the current number of games played (k) is consistent with the wins
        # Let's assume that the current wins are a, b, c
        # Then, a + b + c = k
        # Also, |a - b| = d1, |b - c| = d2
        # We need to find a, b, c such that they are non-negative integers and satisfy the above
        
        # Let's try to find such a, b, c
        # Try all possible combinations of a, b, c that satisfy the conditions
        
        # Try to find a, b, c such that:
        # a + b + c = k
        # |a - b| = d1
        # |b - c| = d2
        # a, b, c >= 0
        
        # Try all possible combinations of a, b, c that satisfy the above conditions
        # We can try to find a, b, c by checking all possible values of b
        found = False
        for b in range(0, k + 1):
            # Try a = b + d1
            a = b + d1
            if a < 0 or a > k:
                continue
            # Try c = b - d2
            c = b - d2
            if c < 0 or c > k:
                continue
            if a + b + c == k:
                found = True
                break
        
        if found:
            results.append("yes")
        else:
            results.append("no")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()