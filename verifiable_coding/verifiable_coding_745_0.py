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
                # The temple has to be symmetric and increase then decrease
                # The length of the temple is (j - i + 1)
                # The middle is at (i + j) // 2
                length = j - i + 1
                mid = (i + j) // 2
                is_valid = True
                for k in range(i, j + 1):
                    # The height at position k should be equal to the distance from the middle
                    # The distance from the middle is abs(k - mid)
                    # The height should be at least that distance
                    if h[k] < abs(k - mid):
                        is_valid = False
                        break
                if is_valid:
                    # Calculate the number of operations needed
                    ops = 0
                    for k in range(i, j + 1):
                        ops += h[k] - abs(k - mid)
                    min_ops = min(min_ops, ops)
        
        results.append(str(min_ops))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()