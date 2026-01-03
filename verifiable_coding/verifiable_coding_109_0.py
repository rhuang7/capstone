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
        m = int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+m]))
        idx += m
        
        from collections import defaultdict
        count = defaultdict(int)
        for num in a:
            count[num] += 1
        
        # Convert counts to log2 for easier handling
        log_count = {}
        for key in count:
            log_count[key] = count[key]
        
        # Try to fill the bag starting from the largest possible power of two
        res = 0
        current = n
        found = False
        
        # Try all possible powers of two up to n
        for power in range(60, -1, -1):
            size = 1 << power
            if size > n:
                continue
            # How many of this size can we use?
            if size in log_count:
                num = log_count[size]
                if num > 0:
                    # Use as many as possible
                    use = min(num, current // size)
                    current -= use * size
                    if current == 0:
                        found = True
                        break
                    # If we have some left, we need to split
                    if use < num:
                        # We can split the remaining ones
                        res += (num - use) * (power - 1)
                        # But we need to track the split sizes
                        # So we need to keep track of the split sizes
                        # So we need to process smaller powers
                        # So we need to break and process smaller powers
                        # So we need to reset the current and proceed
                        current = n
                        found = False
                        break
        if found:
            results.append(res)
        else:
            results.append(-1)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()