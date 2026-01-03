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
            elif i < n:
                a.append(p[k])
                i += 1
                k += 1
            else:
                b.append(p[k])
                j += 1
                k += 1
        if len(a) != n or len(b) != n:
            results.append("NO")
            continue
        valid = True
        for x in a:
            if x in b:
                valid = False
                break
        if not valid:
            results.append("NO")
            continue
        valid = True
        for x in b:
            if x in a:
                valid = False
                break
        if not valid:
            results.append("NO")
            continue
        results.append("YES")
    print('\n'.join(results))