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
        # So total wins is n, and each team has n/3 wins
        if n % 3 != 0:
            results.append("no")
            continue
        total = n // 3
        # Current wins of teams: a, b, c
        # |a - b| = d1, |b - c| = d2
        # a + b + c = k
        # a + b + c + (n - k) = n
        # So (n - k) is the number of remaining games
        rem = n - k
        # We need to find a, b, c such that:
        # a + b + c = k
        # |a - b| = d1
        # |b - c| = d2
        # a + b + c + rem = n
        # a, b, c >= 0
        # Also, a, b, c <= total
        # Try all possible combinations of a, b, c that satisfy the constraints
        found = False
        for a in range(0, total + 1):
            for b in range(0, total + 1):
                if abs(a - b) != d1:
                    continue
                for c in range(0, total + 1):
                    if abs(b - c) != d2:
                        continue
                    if a + b + c == k and a <= total and b <= total and c <= total:
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