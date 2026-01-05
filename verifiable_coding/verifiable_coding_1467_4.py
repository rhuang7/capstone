import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        k = int(data[idx])
        idx += 1
        hints = []
        for _ in range(k):
            op = data[idx]
            li = int(data[idx+1])
            lv = data[idx+2]
            hints.append((op, li, lv))
            idx += 3
        
        # Find the minimal number of lies
        # We need to find a value of n that satisfies as many hints as possible
        # So we try to find the n that satisfies the maximum number of hints
        # Then the minimal lies is k - max_satisfied
        
        # Try all possible n that could be the correct one based on hints
        # But since n can be up to 1e9, we can't try all values
        # Instead, we can collect all possible candidate n values from the hints
        # and check them
        
        candidates = set()
        for op, li, lv in hints:
            if lv == "Yes":
                if op == "<":
                    candidates.add(li - 1)
                elif op == ">":
                    candidates.add(li + 1)
                elif op == "=":
                    candidates.add(li)
        
        # Also consider the boundaries
        # For example, if there is a hint "< 100 Yes", then n could be 99
        # But if there is a hint "> 100 Yes", then n could be 101
        # So we also add 0 and 1e9 + 1 as possible candidates
        candidates.add(0)
        candidates.add(10**9 + 1)
        
        max_satisfied = 0
        for n in candidates:
            satisfied = 0
            for op, li, lv in hints:
                if lv == "Yes":
                    if op == "<":
                        if n < li:
                            satisfied += 1
                    elif op == ">":
                        if n > li:
                            satisfied += 1
                    elif op == "=":
                        if n == li:
                            satisfied += 1
                else:
                    if op == "<":
                        if n >= li:
                            satisfied += 1
                    elif op == ">":
                        if n <= li:
                            satisfied += 1
                    elif op == "=":
                        if n != li:
                            satisfied += 1
            max_satisfied = max(max_satisfied, satisfied)
        
        results.append(str(k - max_satisfied))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()