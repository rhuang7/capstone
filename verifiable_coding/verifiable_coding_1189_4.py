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
            prefix[i + 1] = prefix[i] + A[i]
        for k in range(N):
            # Create B by setting A[k] = 0
            # Compute prefix sums of B
            new_prefix = [0] * (N + 1)
            for i in range(N):
                if i == k:
                    new_prefix[i + 1] = new_prefix[i]
                else:
                    new_prefix[i + 1] = new_prefix[i] + A[i]
            # Find number of ways to split into two non-empty contiguous parts with equal sum
            # We need to find i < j such that new_prefix[j] - new_prefix[i] = 0
            # So new_prefix[j] = new_prefix[i]
            # We can use a set to track seen prefix sums
            seen = set()
            count = 0
            for i in range(N):
                if new_prefix[i] in seen:
                    count += 1
                seen.add(new_prefix[i])
            total += count
        results.append(str(total))
    print('\n'.join(results))