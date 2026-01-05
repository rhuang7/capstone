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
        diff = []
        for i in range(N-1):
            diff.append(A[i] - A[i+1])
        # Find the minimum time when two plants have the same height
        # The time t must satisfy (A[i] - A[i+1]) = (i - (i+1)) * t
        # => (A[i] - A[i+1]) = -t
        # => t = A[i+1] - A[i]
        # But since A is in decreasing order, A[i] > A[i+1], so t = A[i] - A[i+1]
        # But we need to find the minimum t such that for some i, A[i] + i*t = A[i+1] + (i+1)*t
        # => A[i] - A[i+1] = t
        # So t is the difference between A[i] and A[i+1]
        # But we need to find the minimum t such that there exists i where A[i] - A[i+1] = t
        # So the answer is the minimum difference between consecutive elements
        min_t = min(diff)
        results.append(min_t)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()