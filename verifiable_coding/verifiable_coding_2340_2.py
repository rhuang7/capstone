import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = list(map(int, data[idx:idx + 2 * n]))
        idx += 2 * n
        a = []
        b = []
        i = 0
        j = 0
        k = 0
        while k < 2 * n:
            if i < n and j < n:
                if p[k] == p[i]:
                    a.append(p[k])
                    i += 1
                elif p[k] == p[j]:
                    b.append(p[k])
                    j += 1
                else:
                    k += 1
            else:
                if i < n:
                    a.append(p[k])
                    i += 1
                else:
                    b.append(p[k])
                    j += 1
                k += 1
        if len(a) == n and len(b) == n and set(a) & set(b) == set():
            results.append("YES")
        else:
            results.append("NO")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()