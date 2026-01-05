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
        shares = []
        for _ in range(N):
            a = int(data[idx])
            b = int(data[idx + 1])
            idx += 2
            shares.append((a, b))
        # Sort shares by a_i in ascending order and by b_i in descending order
        shares.sort(key=lambda x: (x[0], -x[1]))
        # Find the maximum number of shares that can be sold
        # We can take all shares where b_i is strictly increasing
        count = 1
        max_count = 1
        for i in range(1, N):
            if shares[i][1] > shares[i - 1][1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
        results.append(str(max_count))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()