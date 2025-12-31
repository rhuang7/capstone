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
        prefix = 0
        prefix_sum = [0] * (N + 1)
        for i in range(N):
            prefix_sum[i + 1] = prefix_sum[i] + A[i]
        for k in range(N):
            # Remove A[k] and compute the number of ways to split B into two parts with equal sum
            # B is A with A[k] set to 0
            # The sum of B is prefix_sum[N] - A[k]
            # We need to find the number of ways to split B into two non-empty contiguous parts with equal sum
            # Let sum_B = prefix_sum[N] - A[k]
            # We need to find i < j such that prefix_sum[j] - prefix_sum[i] = sum_B / 2
            # Also, sum_B must be even
            sum_B = prefix_sum[N] - A[k]
            if sum_B % 2 != 0:
                continue
            target = sum_B // 2
            count = 0
            prefix = 0
            for i in range(N):
                prefix += A[i]
                if i == k:
                    prefix = 0
                if prefix == target:
                    count += 1
            total += count
        results.append(total)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()