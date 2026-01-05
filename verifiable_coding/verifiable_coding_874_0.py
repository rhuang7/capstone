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
        M = int(data[idx+1])
        S = int(data[idx+2])
        idx += 3
        H = list(map(int, data[idx:idx+N]))
        idx += N
        H.sort()
        count = 0
        for h in H:
            if h > S:
                continue
            count += 1
            if count > M:
                break
        results.append(str(count))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()