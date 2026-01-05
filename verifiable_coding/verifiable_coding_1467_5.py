import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split(b'\n')
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        k = int(data[idx])
        idx += 1
        hints = []
        for _ in range(k):
            parts = data[idx].split()
            idx += 1
            operator = parts[0]
            li = int(parts[1])
            logical_value = parts[2].decode()
            hints.append((operator, li, logical_value))
        
        # Find the minimal number of lies
        min_lies = 0
        # We need to find a value of n that satisfies as many hints as possible
        # So we try all possible ranges that could be valid for n
        
        # For each hint, we can determine the range of possible n values
        # If the hint is "Yes", then n must satisfy the condition
        # If the hint is "No", then n must not satisfy the condition
        
        # We'll find all possible ranges that could be valid for n
        # and then find the intersection of these ranges
        
        # First, collect all possible ranges for n based on the hints
        ranges = []
        for op, li, lv in hints:
            if lv == 'Yes':
                if op == '<':
                    # n < li
                    ranges.append(( -float('inf'), li))
                elif op == '>':
                    # n > li
                    ranges.append(( li, float('inf')))
                elif op == '=':
                    # n == li
                    ranges.append(( li, li))
            else:
                if op == '<':
                    # n >= li
                    ranges.append(( li, float('inf')))
                elif op == '>':
                    # n <= li
                    ranges.append(( -float('inf'), li))
                elif op == '=':
                    # n != li
                    ranges.append(( -float('inf'), li))
                    ranges.append(( li + 1, float('inf')))
        
        # Now find the intersection of all ranges
        # The intersection is the range that satisfies all hints
        # If there is no intersection, then there is no possible n, but the problem says that there is
        # So we can safely assume that there is at least one possible n
        
        # Find the intersection of all ranges
        # Start with the first range
        low = ranges[0][0]
        high = ranges[0][1]
        
        for i in range(1, len(ranges)):
            current_low, current_high = ranges[i]
            low = max(low, current_low)
            high = min(high, current_high)
        
        # Now find the minimal number of lies
        # We need to find the minimal number of hints that are false
        # For each hint, check if it is true for the chosen n
        # We can choose any n in the intersection range
        # We'll choose n = low (or high, or any in between)
        # We'll check for n = low
        # If low is -inf, we can choose 1
        # If high is inf, we can choose 10^9
        
        # Choose n = low if it's not -inf, else 1
        if low == -float('inf'):
            n = 1
        else:
            n = low
        
        # Now check each hint
        lies = 0
        for op, li, lv in hints:
            if op == '<':
                correct = n < li
            elif op == '>':
                correct = n > li
            elif op == '=':
                correct = n == li
            else:
                correct = False
            if lv == 'Yes' and not correct:
                lies += 1
            elif lv == 'No' and correct:
                lies += 1
        results.append(str(lies))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()