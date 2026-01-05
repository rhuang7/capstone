import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    A = list(map(int, data[idx:idx+N]))
    idx += N
    Q = int(data[idx])
    idx += 1
    queries = list(map(int, data[idx:idx+Q]))
    
    # Precompute all subarrays and their minimums
    min_subarrays = []
    for i in range(N):
        min_val = A[i]
        min_subarrays.append([min_val])
        for j in range(i+1, N):
            min_val = min(min_val, A[j])
            min_subarrays[-1].append(min_val)
    
    # Count occurrences of each minimum
    from collections import defaultdict
    count = defaultdict(int)
    for sub in min_subarrays:
        count[sub[-1]] += 1
    
    # Process queries
    for K in queries:
        print(count.get(K, 0))

if __name__ == '__main__':
    solve()