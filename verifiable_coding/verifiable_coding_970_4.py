import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+N]))
        idx += N
        Q = int(data[idx])
        idx += 1
        queries = []
        for __ in range(Q):
            x = int(data[idx])
            y = int(data[idx+1])
            queries.append((x, y))
            idx += 2
        
        # Preprocess a to be sorted (already sorted as per input constraints)
        # For each query, check if (x, y) lies on any wall
        # A point (x, y) lies on the wall with a_i if x + y = a_i
        # Also, x and y must be >= 0 and <= a_i
        # But since x and y are given as >= 0, and a_i >= 1, we can check x + y == a_i
        # Also, if x + y == a_i, then x and y must be <= a_i (since x + y = a_i and x, y >= 0)
        
        for x, y in queries:
            s = x + y
            if s == 0:
                results.append(0)
                continue
            if s in a:
                results.append(-1)
                continue
            # Find the number of walls with a_i > s
            # Since a is sorted, we can use binary search
            cnt = len(a) - bisect.bisect_right(a, s)
            results.append(cnt)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')