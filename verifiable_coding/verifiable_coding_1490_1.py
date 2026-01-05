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
        a = list(map(int, data[idx:idx+N]))
        idx += N
        count = 0
        a.sort()
        i = 0
        while i < N:
            if i + 1 < N and a[i] == a[i+1]:
                count += 1
                i += 2
            else:
                count += 1
                i += 1
        results.append(str(count))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()