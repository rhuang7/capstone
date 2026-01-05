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
        # Then the minimal number of lies is k - max_satisfied
        
        # We can try all possible n in the range of possible values
        # But since n can be up to 1e9, we need to find the possible range of n
        # based on the hints
        
        # Find the possible range of n
        lower = 1
        upper = 10**9
        
        # Process all hints to find the possible range
        for op, li, lv in hints:
            if lv == "Yes":
                if op == "<":
                    lower = max(lower, li + 1)
                elif op == ">":
                    upper = min(upper, li - 1)
                elif op == "=":
                    lower = max(lower, li)
                    upper = min(upper, li)
            # else: the hint is false, so we don't consider it as correct
        
        # Now find the n in [lower, upper] that satisfies the maximum number of hints
        max_satisfied = 0
        for n in range(lower, upper + 1):
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
            max_satisfied = max(max_satisfied, satisfied)
        
        results.append(str(k - max_satisfied))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()