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
        # Calculate the difference between each pair of adjacent plants
        diff = [A[i] - A[i+1] for i in range(N-1)]
        # Find the minimum time when any two plants have the same height
        # The time for plant i and i+1 to have same height is (A[i] - A[i+1]) / (i+1 - i) = (A[i] - A[i+1]) / 1 = A[i] - A[i+1]
        # But since the plants are growing, we need to find the minimum time when any two plants have same height
        # So we need to find the minimum time when any two plants have same height, which is the minimum of (A[i] - A[i+1]) / (i - (i+1)) = (A[i] - A[i+1]) / (-1) = A[i+1] - A[i]
        # But since we are looking for the minimum time, we need to find the minimum of (A[i+1] - A[i]) / (i - (i+1)) = (A[i+1] - A[i]) / (-1) = A[i] - A[i+1]
        # So we need to find the minimum of (A[i] - A[i+1]) for all i
        # But since the plants are in decreasing order, A[i] > A[i+1], so A[i] - A[i+1] is positive
        # So the minimum time is the minimum of (A[i] - A[i+1]) for all i
        min_time = min(diff)
        results.append(str(min_time))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()