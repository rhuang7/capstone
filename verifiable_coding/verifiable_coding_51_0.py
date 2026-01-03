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
        
        # Total wins after all games must be equal for all teams
        # Let x be the number of wins for each team
        # Total wins = 3x = n => n must be divisible by 3
        if n % 3 != 0:
            results.append("no")
            continue
        
        x = n // 3
        
        # Current wins for teams: a, b, c
        # We have |a - b| = d1, |b - c| = d2
        # Also, a + b + c = k
        # After remaining (n - k) games, total wins will be n, so a + b + c + (n - k) = n => a + b + c = k (already known)
        
        # Possible configurations:
        # Case 1: a = b + d1, b = c + d2
        # Then a = c + d2 + d1, b = c + d2
        # a + b + c = 3c + d1 + 2d2 = k
        # 3c = k - d1 - 2d2
        # c = (k - d1 - 2d2) / 3
        # Must be integer and non-negative
        
        # Case 2: a = b - d1, b = c + d2
        # Then a = c + d2 - d1, b = c + d2
        # a + b + c = 3c + 2d2 - d1 = k
        # 3c = k - 2d2 + d1
        # c = (k - 2d2 + d1) / 3
        # Must be integer and non-negative
        
        # Case 3: a = b + d1, b = c - d2
        # Then a = c - d2 + d1, b = c - d2
        # a + b + c = 3c - d2 + d1 = k
        # 3c = k + d2 - d1
        # c = (k + d2 - d1) / 3
        # Must be integer and non-negative
        
        # Case 4: a = b - d1, b = c - d2
        # Then a = c - d2 - d1, b = c - d2
        # a + b + c = 3c - 2d2 - d1 = k
        # 3c = k + 2d2 + d1
        # c = (k + 2d2 + d1) / 3
        # Must be integer and non-negative
        
        valid = False
        
        # Check case 1
        if (k - d1 - 2 * d2) % 3 == 0:
            c = (k - d1 - 2 * d2) // 3
            if c >= 0:
                a = c + d1 + d2
                b = c + d2
                if a + b + c == k and a <= x and b <= x and c <= x:
                    valid = True
        
        # Check case 2
        if (k - 2 * d2 + d1) % 3 == 0:
            c = (k - 2 * d2 + d1) // 3
            if c >= 0:
                a = c + d2 - d1
                b = c + d2
                if a + b + c == k and a <= x and b <= x and c <= x:
                    valid = True
        
        # Check case 3
        if (k + d2 - d1) % 3 == 0:
            c = (k + d2 - d1) // 3
            if c >= 0:
                a = c - d2 + d1
                b = c - d2
                if a + b + c == k and a <= x and b <= x and c <= x:
                    valid = True
        
        # Check case 4
        if (k + 2 * d2 + d1) % 3 == 0:
            c = (k + 2 * d2 + d1) // 3
            if c >= 0:
                a = c - d2 - d1
                b = c - d2
                if a + b + c == k and a <= x and b <= x and c <= x:
                    valid = True
        
        results.append("yes" if valid else "no")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()