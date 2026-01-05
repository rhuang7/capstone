import sys
import math

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
        M = int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        queries = []
        for _ in range(M):
            queries.append(int(data[idx]))
            idx += 1
        # Precompute all subarrays and their max elements
        # But since N can be up to 1e5, we need an efficient way
        # The key observation is that the p-th subarray is the one with the p-th largest max element
        # So we can collect all max elements of all subarrays, sort them, and answer queries
        max_elements = []
        for i in range(N):
            current_max = A[i]
            for j in range(i, N):
                current_max = max(current_max, A[j])
                max_elements.append(current_max)
        # Sort the max elements in descending order
        max_elements.sort(reverse=True)
        # Answer queries
        for p in queries:
            results.append(str(max_elements[p-1]))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()