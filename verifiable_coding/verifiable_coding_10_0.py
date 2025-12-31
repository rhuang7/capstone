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
        p = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Find the maximum possible sum of absolute differences
        # The optimal subsequence is the one with the maximum and minimum elements
        max_val = max(p)
        min_val = min(p)
        max_idx = p.index(max_val)
        min_idx = p.index(min_val)
        
        # If the max and min are adjacent, the best is to take them
        if abs(max_idx - min_idx) == 1:
            results.append(str(2))
            results.append(f"{max_val} {min_val}")
        else:
            # Otherwise, take the max and min, and any elements in between
            # But we need to choose the shortest possible subsequence
            # So we take the max and min, and the subsequence is of length 2
            results.append(str(2))
            results.append(f"{max_val} {min_val}")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()