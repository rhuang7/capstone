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
        # Preprocess a to be sorted (already sorted as per constraints)
        # For each query, check if (x, y) is on any wall
        # A point (x, y) is on the wall a_i if x + y = a_i
        # Also, check if x == 0 and y == 0 (origin)
        for x, y in queries:
            if x == 0 and y == 0:
                results.append("0")
                continue
            if x + y == 0:
                results.append("-1")
                continue
            if x + y in a:
                results.append("-1")
                continue
            # Find the number of walls with a_i > x + y
            # Since a is sorted, use bisect_right
            cnt = len(a) - bisect.bisect_right(a, x + y)
            results.append(str(cnt))
    print('\n'.join(results))