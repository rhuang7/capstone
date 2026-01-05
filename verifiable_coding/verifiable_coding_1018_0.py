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
        
        # Find the minimum time when any two plants have the same height
        # The time for plant i to catch up to plant i+1 is (diff) / (i - (i+1)) = diff / (-1) = -diff
        # But since we want the minimum positive time, we take the absolute value of diff
        min_time = min(diffs)
        results.append(min_time)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()