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
        W = list(map(int, data[idx:idx+N]))
        idx += N
        max_w = max(W)
        count = 0
        for i in range(N):
            if W[i] == max_w:
                count += 1
        res = 0
        for k in range(N):
            shift = k
            first_half = W[k:] + W[:k]
            max_in_first = max(first_half)
            if max_in_first != max_w:
                res += 1
        results.append(res)
    for r in results:
        print(r)

if __name__ == '__main__':
    solve()