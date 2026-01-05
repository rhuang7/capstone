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
            # Set A[k] to 0
            new_prefix = [0] * (N + 1)
            for i in range(N):
                if i == k:
                    new_prefix[i + 1] = new_prefix[i]
                else:
                    new_prefix[i + 1] = new_prefix[i] + A[i]
            # Find number of ways to split into two non-empty contiguous parts with equal sum
            count = 0
            for i in range(1, N):
                for j in range(i + 1, N + 1):
                    if new_prefix[j] - new_prefix[i] == 0:
                        count += 1
            total += count
        results.append(total)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()