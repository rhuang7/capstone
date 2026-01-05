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
        # and find the minimum time when their heights become equal
        # The difference between A[i] and A[i+1] is (A[i] - A[i+1])
        # The growth rates are i and i+1
        # So, the time when they become equal is (A[i] - A[i+1]) / (i+1 - i) = (A[i] - A[i+1]) / 1
        # But since the growth is in increasing order, we need to check for the minimum time when any two plants have the same height
        # We can use a set to track the heights of the plants at each time step
        # But for large N, this is not efficient
        # Instead, we can compute for each pair of plants (i, j) where i < j
        # The time when their heights become equal is (A[i] - A[j]) / (j - i)
        # We need to find the minimum such time across all pairs
        # But for N up to 1e5, this is O(N^2), which is not feasible
        # So we need a better approach
        # Let's consider the difference between consecutive plants
        # For each i from 0 to N-2:
        # The time when A[i] and A[i+1] become equal is (A[i] - A[i+1]) / (i+1 - i) = A[i] - A[i+1]
        # Since the plants are in decreasing order, A[i] > A[i+1]
        # So the time is positive
        # We can compute this for each consecutive pair and take the minimum
        min_time = float('inf')
        for i in range(N-1):
            diff = A[i] - A[i+1]
            time = diff
            if time < min_time:
                min_time = time
        results.append(str(min_time))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()