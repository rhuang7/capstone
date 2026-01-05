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
        n = int(data[idx])
        idx += 1
        h = list(map(int, data[idx:idx + n]))
        idx += n
        
        min_ops = float('inf')
        
        for i in range(n):
            for j in range(i, n):
                # Check if the subarray from i to j can form a temple
                # The temple must be symmetric and form a peak
                # Check if the subarray is symmetric and forms a valid temple
                is_valid = True
                peak = (i + j) // 2
                for k in range(i, j + 1):
                    if k < peak:
                        if h[k] < h[peak] - (peak - k):
                            is_valid = False
                            break
                    elif k > peak:
                        if h[k] < h[peak] - (k - peak):
                            is_valid = False
                            break
                    else:
                        # peak is at the middle
                        pass
                if is_valid:
                    # Calculate the number of operations needed
                    ops = 0
                    for k in range(i, j + 1):
                        if k < peak:
                            ops += h[k] - (h[peak] - (peak - k))
                        elif k > peak:
                            ops += h[k] - (h[peak] - (k - peak))
                    min_ops = min(min_ops, ops)
        
        results.append(str(min_ops))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()