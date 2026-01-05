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
            idx += 3
            hints.append((op, li, lv))
        
        # Find the minimal number of lies
        min_lies = 0
        # Try all possible n in the range of possible values
        # We need to find the range of possible n based on the hints
        # But since n can be up to 1e9, we can't iterate through all possible n
        # Instead, we find the possible range of n that satisfies the hints
        # and then check for the minimal lies in that range
        
        # Find the possible range of n
        lower = 1
        upper = 10**9
        
        for op, li, lv in hints:
            if lv == "Yes":
                if op == "<":
                    lower = max(lower, li + 1)
                elif op == ">":
                    upper = min(upper, li - 1)
                elif op == "=":
                    lower = max(lower, li)
                    upper = min(upper, li)
            else:
                if op == "<":
                    # The hint is false, so n >= li
                    lower = max(lower, li)
                elif op == ">":
                    # The hint is false, so n <= li
                    upper = min(upper, li)
                elif op == "=":
                    # The hint is false, so n != li
                    lower = max(lower, li + 1)
                    upper = min(upper, li - 1)
        
        # If lower > upper, no possible n
        if lower > upper:
            results.append(0)
            continue
        
        # Now find the minimal number of lies in the possible range
        # We can try all possible n in the range and count the lies
        # But since n can be up to 1e9, we need to find the minimal lies
        # by checking the possible n that satisfies the hints
        
        # Find the minimal number of lies
        min_lies = float('inf')
        # Try all possible n in the range
        # But since n can be up to 1e9, we need to find the minimal lies
        # by checking the possible n that satisfies the hints
        
        # We can try the lower and upper bounds
        for n in [lower, upper]:
            lies = 0
            for op, li, lv in hints:
                if lv == "Yes":
                    if op == "<":
                        if n >= li:
                            lies += 1
                    elif op == ">":
                        if n <= li:
                            lies += 1
                    elif op == "=":
                        if n != li:
                            lies += 1
                else:
                    if op == "<":
                        if n < li:
                            lies += 1
                    elif op == ">":
                        if n > li:
                            lies += 1
                    elif op == "=":
                        if n == li:
                            lies += 1
            min_lies = min(min_lies, lies)
        
        results.append(min_lies)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()