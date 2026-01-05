import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        type_ = int(data[idx])
        idx += 1
        s = data[idx]
        idx += 1
        n = len(s)
        
        # Check if it's possible to rearrange
        count_b = s.count('B')
        count_g = n - count_b
        if abs(count_b - count_g) > 1:
            results.append("-1")
            continue
        
        # Prepare list of positions for B and G
        b_pos = [i for i, c in enumerate(s) if c == 'B']
        g_pos = [i for i, c in enumerate(s) if c == 'G']
        
        # Determine target arrangement
        if count_b > count_g:
            # More B's, need to place B's in even positions
            target = ['B' if i % 2 == 0 else 'G' for i in range(n)]
        else:
            # More G's, need to place G's in even positions
            target = ['G' if i % 2 == 0 else 'B' for i in range(n)]
        
        # Check if current arrangement is already valid
        valid = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                valid = False
                break
        if valid:
            results.append("0")
            continue
        
        # Find mismatches
        mismatch_b = []
        mismatch_g = []
        for i in range(n):
            if s[i] == 'B' and target[i] == 'G':
                mismatch_b.append(i)
            elif s[i] == 'G' and target[i] == 'B':
                mismatch_g.append(i)
        
        # If no mismatches, already valid
        if not mismatch_b and not mismatch_g:
            results.append("0")
            continue
        
        # If there are mismatches, we need to swap
        # For type 0, cost is 1 per swap
        # For type 1, cost is |i - j|
        # For type 2, cost is (i - j)^2
        
        # We need to pair B's with G's in mismatch_b and mismatch_g
        # To minimize cost, we should pair the first B with first G, etc.
        # So sort the mismatch_b and mismatch_g
        mismatch_b.sort()
        mismatch_g.sort()
        
        # Pair them
        swaps = []
        for i in range(len(mismatch_b)):
            b = mismatch_b[i]
            g = mismatch_g[i]
            swaps.append((b, g))
        
        # Calculate cost
        total_cost = 0
        for b, g in swaps:
            if type_ == 0:
                total_cost += 1
            elif type_ == 1:
                total_cost += abs(b - g)
            elif type_ == 2:
                total_cost += (b - g) ** 2
        
        results.append(str(total_cost))
    
    print("\n".join(results))