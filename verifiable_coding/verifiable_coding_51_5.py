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
        # Let the final wins be x for each team
        # Total wins = 3x = n => n must be divisible by 3
        if n % 3 != 0:
            results.append("no")
            continue
        
        x = n // 3
        
        # Current wins of teams: a, b, c
        # We have |a - b| = d1, |b - c| = d2
        # Also, a + b + c = k
        # After all games: a + (n - k) = x, same for b and c
        # So a = x - (n - k), b = x - (n - k), c = x - (n - k)
        # But this is not correct, because the current wins are a, b, c and we have to add (n - k) games
        
        # Let's think differently: the final wins must be x for each team
        # So the total wins after all games is 3x = n
        # The current wins are a, b, c such that a + b + c = k
        # And |a - b| = d1, |b - c| = d2
        
        # We can try all possible combinations of a, b, c that satisfy the conditions
        # Let's try all possible combinations of a, b, c such that a + b + c = k and |a - b| = d1, |b - c| = d2
        
        # Try all possible values of b
        found = False
        for b in range(0, k + 1):
            # Try a = b + d1 or a = b - d1
            for a in [b + d1, b - d1]:
                if a < 0 or a > k:
                    continue
                # Try c = b + d2 or c = b - d2
                for c in [b + d2, b - d2]:
                    if c < 0 or c > k:
                        continue
                    if a + b + c == k:
                        # Check if after adding (n - k) games, all teams have x wins
                        # a + (n - k) = x => a = x - (n - k)
                        # b + (n - k) = x => b = x - (n - k)
                        # c + (n - k) = x => c = x - (n - k)
                        # So a = b = c = x - (n - k)
                        # So a must be equal to b and c
                        if a == b == c:
                            found = True
                            break
                if found:
                    break
            if found:
                break
        
        results.append("yes" if found else "no")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()