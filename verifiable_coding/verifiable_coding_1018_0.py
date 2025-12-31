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
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Calculate the difference between each pair of consecutive plants
        diffs = []
        for i in range(N-1):
            diff = A[i] - A[i+1]
            diffs.append(diff)
        
        # Find the minimum time when two plants have the same height
        # For each pair, the time when they meet is (diff) / (i - (i+1)) = diff / (-1) = -diff
        # But since we want the minimum positive time, we take the absolute value
        min_time = min(abs(diff) for diff in diffs)
        results.append(str(min_time))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()