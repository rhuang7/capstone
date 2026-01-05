import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx+1])
        d1 = int(data[idx+2])
        d2 = int(data[idx+3])
        idx += 4
        
        # Total wins after all games must be n
        # Let x, y, z be the wins of teams 1, 2, 3
        # x + y + z = n
        # |x - y| = d1
        # |y - z| = d2
        # Also, x, y, z >= 0
        # And x, y, z must be such that all teams have equal wins at the end
        # So x = y = z = n / 3
        # But since n may not be divisible by 3, we need to check if it is possible
        if n % 3 != 0:
            results.append("no")
            continue
        
        target = n // 3
        
        # Check if there exists a way to distribute the wins such that the differences are d1 and d2
        # Also, the current wins (from the k games) must be such that the remaining games can be played to reach the target
        # Let a, b, c be the current wins of the teams
        # a + b + c = k
        # |a - b| = d1
        # |b - c| = d2
        # Also, a, b, c >= 0
        # And after (n - k) games, the total wins of each team must be target
        
        # Try all possible combinations of a, b, c that satisfy the conditions
        # Since the differences are fixed, we can try possible values for a, b, c
        # Let's try all possible a, b, c that satisfy |a - b| = d1 and |b - c| = d2
        # Also, a + b + c = k
        # And a, b, c >= 0
        
        found = False
        for a in range(0, k + 1):
            for b in range(0, k + 1):
                if abs(a - b) != d1:
                    continue
                for c in range(0, k + 1):
                    if abs(b - c) != d2:
                        continue
                    if a + b + c == k:
                        # Check if the remaining games can be played to reach target
                        # After (n - k) games, each team must have target wins
                        # So remaining wins for each team is target - a, target - b, target - c
                        # These must be non-negative and sum to (n - k)
                        rem_a = target - a
                        rem_b = target - b
                        rem_c = target - c
                        if rem_a < 0 or rem_b < 0 or rem_c < 0:
                            continue
                        if rem_a + rem_b + rem_c == n - k:
                            found = True
                            break
                if found:
                    break
            if found:
                break
        
        results.append("yes" if found else "no")
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()