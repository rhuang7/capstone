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
        h = list(map(int, data[idx:idx+n]))
        idx += n
        
        min_ops = float('inf')
        
        for i in range(n):
            for j in range(i, n):
                # Check if the subarray from i to j can form a temple
                # The temple must be symmetric and have increasing then decreasing pattern
                # The length of the temple is (j - i + 1)
                # The middle is at (i + j) // 2
                # The maximum height is (j - i + 1) // 2 + 1
                length = j - i + 1
                max_height = (length + 1) // 2
                ops = 0
                for k in range(i, j + 1):
                    expected = max_height - abs(k - (i + j) // 2)
                    ops += max(0, h[k] - expected)
                min_ops = min(min_ops, ops)
        
        results.append(str(min_ops))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()