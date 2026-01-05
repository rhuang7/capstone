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
        if count == 0:
            results.append(0)
        else:
            results.append(N // 2)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()