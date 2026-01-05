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
        K = int(data[idx+1])
        idx += 2
        forgotten = data[idx:idx+N]
        idx += N
        modern = set()
        for _ in range(K):
            L = int(data[idx])
            idx += 1
            for _ in range(L):
                modern.add(data[idx])
                idx += 1
        res = []
        for word in forgotten:
            res.append("YES" if word in modern else "NO")
        results.append(" ".join(res))
    print("\n".join(results))

if __name__ == '__main__':
    solve()