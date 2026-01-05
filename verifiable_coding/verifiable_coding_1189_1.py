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
        total = 0
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i+1] = prefix[i] + A[i]
        for k in range(N):
            # Create B by setting A[k] = 0
            # Compute prefix sums for B
            new_prefix = [0] * (N + 1)
            for i in range(N):
                if i == k:
                    new_prefix[i+1] = new_prefix[i]
                else:
                    new_prefix[i+1] = new_prefix[i] + A[i]
            # Find number of ways to split B into two non-empty contiguous parts with equal sum
            # We need to find i < j such that new_prefix[j] - new_prefix[i] = (new_prefix[N] - new_prefix[i]) / 2
            # Which simplifies to new_prefix[j] = new_prefix[N] / 2 + new_prefix[i]
            # So for each i, check if (new_prefix[N] - new_prefix[i]) is even and if (new_prefix[N] - new_prefix[i]) / 2 exists in new_prefix
            # But since we are looking for j > i, we can use a set to store prefix sums
            prefix_set = set()
            count = 0
            target = new_prefix[N] // 2
            for i in range(N):
                if (new_prefix[N] - new_prefix[i]) % 2 == 0:
                    if (new_prefix[N] - new_prefix[i]) // 2 in prefix_set:
                        count += 1
                prefix_set.add(new_prefix[i])
            total += count
        results.append(total)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()