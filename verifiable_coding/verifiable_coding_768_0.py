import sys
import sys
input = sys.stdin.buffer.read
def solve():
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        p = list(map(int, data[idx:idx + N - 1]))
        idx += N - 1
        # Build the tree
        from collections import defaultdict
        tree = defaultdict(list)
        for i in range(1, N):
            tree[p[i - 1]].append(i)
        # Compute the maximum sum of MEX
        # The maximum sum is N*(N-1)//2
        results.append(N * (N - 1) // 2)
    for res in results:
        print(res)
if __name__ == '__main__':
    solve()