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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        S = list(map(int, data[idx:idx+N]))
        idx += N
        S.sort(reverse=True)
        cutoff = S[K-1]
        count = 0
        for s in S:
            if s >= cutoff:
                count += 1
            else:
                break
        results.append(str(count))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()