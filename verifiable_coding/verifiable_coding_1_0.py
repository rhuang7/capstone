import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    q = int(data[0])
    index = 1
    results = []
    
    for _ in range(q):
        n = int(data[index])
        m = int(data[index+1])
        k = int(data[index+2])
        index += 3
        
        # Total steps needed to reach (n, m)
        # Each diagonal move contributes 1 to both x and y
        # Each non-diagonal move contributes 1 to either x or y
        # Let d be the number of diagonal moves
        # Then, d + s = k, where s is the number of non-diagonal moves
        # Also, d + s_x = n, d + s_y = m, where s_x and s_y are the number of non-diagonal moves in x and y directions
        # So, s_x = n - d, s_y = m - d
        # Total non-diagonal moves: s = s_x + s_y = n + m - 2d
        # Also, s = k - d
        # So, k - d = n + m - 2d
        # => k = n + m - d
        # => d = n + m - k
        
        d = n + m - k
        if d < 0:
            results.append(-1)
            continue
        
        # Check if d is feasible
        # The maximum possible diagonal moves is min(n, m)
        # The minimum possible diagonal moves is max(0, (n + m - k) - (k - max(n, m)))
        # Also, the number of non-diagonal moves must be non-negative
        # s_x = n - d >= 0
        # s_y = m - d >= 0
        # Also, s = k - d >= 0
        # So, d <= min(n, m)
        # And d >= max(0, (n + m - k) - (k - max(n, m)))
        
        if d > min(n, m):
            results.append(-1)
            continue
        
        # Check if the number of non-diagonal moves is non-negative
        s = k - d
        if s < 0:
            results.append(-1)
            continue
        
        # Check if s_x and s_y are non-negative
        s_x = n - d
        s_y = m - d
        if s_x < 0 or s_y < 0:
            results.append(-1)
            continue
        
        # Check if s_x + s_y == s
        if s_x + s_y != s:
            results.append(-1)
            continue
        
        # Check if the total steps is exactly k
        if d + s != k:
            results.append(-1)
            continue
        
        # If all conditions are satisfied, then d is the maximum number of diagonal moves
        results.append(d)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()