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
        # Let total wins be x, so 3x = n
        if n % 3 != 0:
            results.append("no")
            continue
        
        x = n // 3
        
        # Current wins of teams: a, b, c
        # |a - b| = d1, |b - c| = d2
        # a + b + c = k
        # a + b + c + (n - k) = n
        # a + b + c = k
        # a + b + c + (n - k) = n
        # So, the remaining (n - k) games must be distributed such that all teams end up with x wins
        
        # Let's find possible a, b, c such that:
        # |a - b| = d1
        # |b - c| = d2
        # a + b + c = k
        # a + b + c + (n - k) = n
        # a + b + c = k
        # a + b + c + (n - k) = n
        # So, the remaining (n - k) games must be distributed such that all teams end up with x wins
        
        # Try all possible combinations of a, b, c that satisfy the constraints
        found = False
        for a in range(0, k + 1):
            for b in range(0, k + 1):
                if abs(a - b) != d1:
                    continue
                for c in range(0, k + 1):
                    if abs(b - c) != d2:
                        continue
                    if a + b + c != k:
                        continue
                    # Check if it's possible to reach x wins for all teams with remaining games
                    remaining = n - k
                    if (x - a) + (x - b) + (x - c) != remaining:
                        continue
                    found = True
                    break
                if found:
                    break
            if found:
                break
        
        results.append("yes" if found else "no")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()