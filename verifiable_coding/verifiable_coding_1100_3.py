import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        p = int(data[idx])
        q = int(data[idx+1])
        r = int(data[idx+2])
        idx += 3
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])
        idx += 3
        
        # Check if the target is achievable
        if (a < p and b < q and c < r) or (a > p and b > q and c > r):
            results.append("-1")
            continue
        
        # Check if the target is achievable by adding the same value to all elements
        diff_p = a - p
        diff_q = b - q
        diff_r = c - r
        
        # Check if all differences are non-negative and same
        if diff_p >= 0 and diff_q >= 0 and diff_r >= 0:
            if diff_p == diff_q == diff_r:
                results.append(str(diff_p))
                continue
        
        # Check if the target is achievable by adding different values to different elements
        # Case 1: add to p and q
        if diff_p >= 0 and diff_q >= 0 and diff_r == 0:
            results.append(str(diff_p + diff_q))
            continue
        
        # Case 2: add to p and r
        if diff_p >= 0 and diff_r >= 0 and diff_q == 0:
            results.append(str(diff_p + diff_r))
            continue
        
        # Case 3: add to q and r
        if diff_q >= 0 and diff_r >= 0 and diff_p == 0:
            results.append(str(diff_q + diff_r))
            continue
        
        # Case 4: add to p
        if diff_p >= 0 and diff_q == 0 and diff_r == 0:
            results.append(str(diff_p))
            continue
        
        # Case 5: add to q
        if diff_q >= 0 and diff_p == 0 and diff_r == 0:
            results.append(str(diff_q))
            continue
        
        # Case 6: add to r
        if diff_r >= 0 and diff_p == 0 and diff_q == 0:
            results.append(str(diff_r))
            continue
        
        # If none of the above cases work
        results.append("-1")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()