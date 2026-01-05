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
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Find all positions where the element is missing
        missing = []
        for i in range(n):
            if a[i] == -1:
                missing.append(i)
        
        # For each missing position, find the possible values of k that can minimize the max difference
        # We need to find the k that minimizes the maximum of |a[i] - k| and |k - a[i+1]|
        # For each pair of adjacent non-missing elements, the k must be in the range [min_val, max_val]
        # We can collect all such ranges and find the k that is in the intersection of all ranges
        
        # Collect all possible ranges for k
        ranges = []
        for i in range(len(missing) - 1):
            left = missing[i]
            right = missing[i + 1]
            # The k must be between a[left] and a[right] to minimize the max difference
            # But since a[left] and a[right] are not missing, we can use them
            lower = min(a[left], a[right])
            upper = max(a[left], a[right])
            ranges.append((lower, upper))
        
        # If there are no ranges (only one missing element), then k can be anything
        if not ranges:
            # The maximum difference is between the two missing elements
            # So k can be any value between a[0] and a[1]
            lower = min(a[0], a[1])
            upper = max(a[0], a[1])
            ranges = [(lower, upper)]
        
        # Find the intersection of all ranges
        # The intersection is the maximum of all lower bounds and the minimum of all upper bounds
        lower = max(r[0] for r in ranges)
        upper = min(r[1] for r in ranges)
        
        # If lower > upper, then there is no possible k, but the problem states that at least one element is missing
        # So this case should not happen
        # Choose k as the middle of the range (or any value in the range)
        k = (lower + upper) // 2
        
        # Now, compute the maximum absolute difference between adjacent elements
        max_diff = 0
        for i in range(n - 1):
            if a[i] == -1:
                a[i] = k
            if a[i + 1] == -1:
                a[i + 1] = k
            diff = abs(a[i] - a[i + 1])
            if diff > max_diff:
                max_diff = diff
        
        results.append(f"{max_diff} {k}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()