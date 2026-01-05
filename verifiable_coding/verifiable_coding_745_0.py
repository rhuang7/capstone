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
                # The temple must be symmetric and start from 1, increase by 1, then decrease by 1
                # The length of the temple is (j - i + 1)
                # The middle of the temple is at (i + j) // 2
                length = j - i + 1
                if length % 2 == 0:
                    continue  # Cannot form a temple with even length
                mid = (i + j) // 2
                valid = True
                for k in range(i, j + 1):
                    # The height at position k should be equal to the distance from k to mid
                    # For example, at mid, it should be 1, at mid-1 and mid+1 it should be 2, etc.
                    dist = abs(k - mid)
                    if h[k] < dist:
                        valid = False
                        break
                if valid:
                    # Calculate the number of operations needed
                    ops = 0
                    for k in range(i, j + 1):
                        dist = abs(k - mid)
                        ops += (h[k] - dist)
                    min_ops = min(min_ops, ops)
        
        results.append(str(min_ops))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()