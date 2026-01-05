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
        current_min = A[i]
        min_subarrays.append(current_min)
        for j in range(i+1, N):
            current_min = min(current_min, A[j])
            min_subarrays.append(current_min)
    
    # Prepare a frequency dictionary
    freq = {}
    for m in min_subarrays:
        if m in freq:
            freq[m] += 1
        else:
            freq[m] = 1
    
    # Process queries
    for K in queries:
        print(freq.get(K, 0))

if __name__ == '__main__':
    solve()