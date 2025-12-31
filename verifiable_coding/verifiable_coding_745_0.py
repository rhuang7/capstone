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
                # The temple must be symmetric and form the pattern 1,2,...,x,...,2,1
                # Check if the subarray is symmetric and forms the required pattern
                # The length of the subarray must be odd
                length = j - i + 1
                if length % 2 == 0:
                    continue
                x = (length - 1) // 2
                valid = True
                for k in range(length):
                    expected = x - abs(k - x)
                    if h[i + k] < expected:
                        valid = False
                        break
                if valid:
                    # Calculate the number of operations needed
                    ops = 0
                    for k in range(length):
                        expected = x - abs(k - x)
                        ops += h[i + k] - expected
                    min_ops = min(min_ops, ops)
        
        results.append(str(min_ops))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()