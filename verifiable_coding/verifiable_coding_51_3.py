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
        
        # Total wins after n games must be equal for all teams
        # So total wins = n, and each team has n/3 wins
        if n % 3 != 0:
            results.append("no")
            continue
        total = n // 3
        # Current wins of teams: a, b, c
        # We have |a - b| = d1, |b - c| = d2
        # Also, a + b + c = k
        # And a + b + c + remaining = n
        # remaining = n - k
        # So a + b + c = k
        # We need to find a, b, c such that:
        # |a - b| = d1
        # |b - c| = d2
        # a + b + c = k
        # a + b + c + remaining = n
        # remaining = n - k
        # Also, a, b, c must be non-negative integers
        # We can try all possible combinations of a, b, c that satisfy the above conditions
        # Try all possible a, b, c that satisfy |a - b| = d1 and |b - c| = d2 and a + b + c = k
        found = False
        for a in range(0, k + 1):
            for b in range(0, k + 1):
                if abs(a - b) != d1:
                    continue
                for c in range(0, k + 1):
                    if abs(b - c) != d2:
                        continue
                    if a + b + c == k:
                        # Check if remaining games can be played to make all teams have total wins = total
                        # remaining = n - k
                        # a + remaining1 = total
                        # b + remaining2 = total
                        # c + remaining3 = total
                        # remaining1 + remaining2 + remaining3 = remaining
                        # remaining1 = total - a
                        # remaining2 = total - b
                        # remaining3 = total - c
                        # total_remaining = (total - a) + (total - b) + (total - c)
                        # total_remaining = 3 * total - (a + b + c)
                        # total_remaining = 3 * total - k
                        # remaining = n - k
                        # So 3 * total - k must be equal to remaining
                        # total = n // 3
                        # remaining = n - k
                        # So 3 * total - k = remaining
                        # which is always true because total = n // 3
                        # So check if all remaining wins are non-negative
                        if (total - a) >= 0 and (total - b) >= 0 and (total - c) >= 0:
                            found = True
                            break
                if found:
                    break
            if found:
                break
        results.append("yes" if found else "no")
    print("\n".join(results))

if __name__ == '__main__':
    solve()